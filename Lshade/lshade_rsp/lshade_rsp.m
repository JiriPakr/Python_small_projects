clear;clc;close all;
%{
Implementation of LSHADE with rank based mutation stategy inspired by:
https://ieeexplore.ieee.org/abstract/document/8477977
%}

%% Init
dim=2;                                  % problem dimension - only designed for dim=2
H = 5;                                  % memory size
H_curr = 1;                             % current memory cell for updating
k = 3;                                  % rank greediness factor
D = 20;
Nmin = 4; Nmax = round(75 * D^(2/3));   % min and max population size
lim_rast=[-5.12, 5.12;-5.12, 5.12];     % bounds for rastrigin function
lim_rosen = [-2,2;-1,3];                % bounds for rosenbrock function
lim_schaffer = [-50,50;-50,50];         % bounds for schaffer N. 2 function
uF = 0.3; uCr = 0.8;                    % initial values of F and Cr
NFE = 0;                                % current number of function evaluations
NFE_max =50;                            % maximal number of function evaluations
g = 1;                                  % generation number
NP = zeros(NFE_max,1); NP(1)=Nmax;      % population size vector - value according to generation

A = zeros(NP(g),dim);                   % Archive set
M_F = ones(H,1);                        % allocating memory for F
M_Cr = ones(H,1);                       % allocating memory for Cr

%func = @(x,y) rastrigin(x,y);          % Rastrigin function call
%lim = lim_rast;                        % setting current bonds to rastrigin

%func = @(x,y) rosenbrock(x,y);         % Rosenbrock function call
%lim = lim_rosen;

func = @(x,y) schaffer(x,y);           % Schaffel function call
lim = lim_schaffer;

% init solution
x = zeros(NP(g),dim);                   % population
for i = 1:dim
    x(:,i) = lim(i,1) + rand(NP(g), 1) * (lim(i,2)-lim(i,1));
end
t = zeros(NP(g), dim);                  % trial vectors
fx = func(x(:,1) ,x(:,2) );             % eval values
%fval_hist = [];
%x_hist = [];
tic
%% Main loop
    while NFE < NFE_max
        M_F = M_F * uF;
        M_Cr = M_Cr * uCr;
        NFE = NFE + 1;
        
            for i=1:length(x)
                if i > length(x)
                    i = length(x);
                end
                %eval 
                fx = func(x(:,1) ,x(:,2) );
                [best_value, best_idx] = min(fx);
                fval = fx(best_idx);                % best idx eval
                found_min = x(best_idx,:);          % pop on best idx
                %fval_hist = [fval_hist(1:end), fval];
                %x_hist = [x_hist(1:end), x_out];

                % generating random_idx of H
                r_idx = round(1 + rand() * (H-1));
                % one value of M_F or M_Cr must be = 0.9
                if isempty(find(M_F == 0.9,1))
                    M_F(end) = 0.9;
                end
                if isempty(find(M_Cr == 0.9,1))
                    M_Cr(end) = 0.9;
                end
                if r_idx == H
                    % generating F from standard Cauchy distribution using trnd(1) (trnd is Student's t distribution)  
                    F = 0.1 + trnd(1) * (0.9-0.1);
                    % generating Cr with normal distribution 
                    Cr = 0.1 + rand() * (0.9-0.1);
                else               
                    F = 0.1 + trnd(1) * (M_F(r_idx)-0.1);
                    Cr = 0.1 + rand() * (M_Cr(r_idx)-0.1);
                end
                if Cr < 0
                    Cr = 0;
                end

                if NFE < 0.25*NFE_max
                    Cr = max(M_Cr(r_idx),0.7);
                elseif NFE < 0.5*NFE_max
                    Cr = max(M_Cr(r_idx),0.6);
                end

                %% Mutation + setup
                Fw = choose_fw(F,NFE,NFE_max);
                fx_sorted = sort(fx,'descend');

                % rank choose for rank-based mutation
                Ranks = rankcalc(k,length(x));
                prs = prcalc(Ranks,length(x));
                Prob_intervals = probintervalcalc(prs,length(x));
                rnum1 = rand("double"); rnum2 = rand("double");
                % chosen values
                pr1 = find(Prob_intervals < rnum1,1) +1;
                pr2 = find(Prob_intervals < rnum2,1) +1;
                if pr1 == length(x) + 1
                    pr1 = length(x);
                end
                if pr2 == length(x) + 1
                    pr2 = length(x);
                end
                
                % random numbers for crossover generated ahead
                r = rand(length(x), dim);
                R = randi([1, dim], length(x), 1);
                t(:, :) = x(:, :);  % copy values, overwrite only when crossover
                for j=1:dim
                    % mutant vector
                    v(j) = x(i,j) + Fw*(x(best_idx,j) - x(i,j)) + F*(x(pr1,j) - x(pr2,j));
                    %% crossover
                    if i == R(i) || r(i, j) < Cr  
                        if lim(j,1) <= v(j) && lim(j,2) <= v(j)
                            t(i, j) = v(j);
                        else
                            t(i, j) = lim(j,1) + rand() * (lim(j,2)-lim(j,1));
                        end
                    end
                end
                %% selection
                ft = func(t(:,1),t(:,2));
                is_better = ft < fx;
                x(is_better, :) = t(is_better, :);
                fx(is_better) = ft(is_better);
                % Archive
                A = [A(1:end),x(is_better)];
                M_F(H_curr) = F;
                M_Cr(H_curr) = Cr;
                H_curr = H_curr + 1;
                if H_curr == 5
                    H_curr = 1;
                end
                %% Update
                % pop
                
                while ~(length(x) < NP(g))
                    fx = func(x(:,1) ,x(:,2) );
                    worst_value = max(fx);
                    worst_idxs = find(fx == worst_value);
                    x(worst_idxs,:) = [];
                    t(worst_idxs,:) = [];
                end
                NP(g+1) = round((Nmin - Nmax)/NFE_max * NFE+Nmax);
                
                % archive
                if length(A) >= 1 && length(x) == NP(g)
                    A_len = length(A);
                    rnd_a_idx = round(1 + rand() * (A_len-1));
                    A(rnd_a_idx) = [];
                end
                % uF, uCr
                
                mean_F = sum(M_F)/length(M_F);
                mean_Cr = sum(M_Cr)/length(M_Cr);
                M_F(r_idx) = mean_F;
                M_Cr(r_idx) =  mean_Cr;
            end
            g = g + 1;
            % updating using lehmer mean once per generation
            p = 4;
            lehmer_mean_F = (sum(M_F)^p)/(sum(M_F)^(p-1));
            lehmer_mean_Cr = (sum(M_Cr)^p)/(sum(M_Cr)^(p-1));
            M_F(r_idx) = mean_F;
            M_Cr(r_idx) =  mean_Cr;
    end

found_min
toc
%% plots
x_plot = linspace(lim(1,1),lim(1,2),NP(1));
y_plot = linspace(lim(2,1),lim(2,2),NP(1));
for i = 1:length(x_plot)
    for j = 1:length(y_plot)
        z_plot(i,j) = func(x_plot(i),y_plot(j));
    end
end
contour(x_plot,y_plot,z_plot',"LineWidth",0.5)
hold on
plot(found_min(1),found_min(2),'rx')

%% Other functions
    function Fw = choose_fw(F,NFE,NFE_max)
        if  NFE < 0.2*NFE_max
            Fw = 0.7*F;
        elseif NFE >= 0.2*NFE_max && NFE < 0.4*NFE_max
            Fw = 0.8*F;
        else
            Fw = 1.2*F;
        end
    end

    function Rank = rankcalc(k,NP)
        Rank = zeros(1,NP);
        for i=1:NP        
            Rank(i) = k * (NP - i) + 1;
        end
    end

    function pr = prcalc(Rank,NP)
    pr = zeros(1,NP);
    for i = 1:NP
        pr(i) = Rank(i)/(sum(Rank));
    end
    end

    function Prob_intervals = probintervalcalc(pr,NP)
    Prob_intervals = zeros(1,NP);
    Prob_intervals(1) = 1 - pr(1);
    for i =2:NP
        Prob_intervals(i) = Prob_intervals(i-1) - pr(i);
    end
    end