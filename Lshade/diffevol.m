%%     Differential Evolution
%    https://en.wikipedia.org/wiki/Differential_evolution
%    :param func: objective function
%    :param dim: problem dimension
%    :param lim: limits - 2 values
%    :param NP: population size
%    :param F: differential weight 0 <= F <= 2
%    :param CR: crossover probability 0 <= CR <= 1
%    :param max_iter: maximum number of iterations
%    :param max_iter_eps: maximum number of iterations where fval
%                         does not change by epsilon
%    :param epsilon: value for max_iter_eps
%    :return: x_out:vector, fval:function value in x_out
% Octave needs for randsample:  pkg install -forge io statistics

function [x_out, fval] = diffevol(func, dim, lim, NP, F, CR, max_iter, max_iter_eps, epsilon)
    choices_cache = zeros(NP, NP-1);
    one_to_NP = 1:NP;
    for j=1:NP
        choices_cache(j, :) = one_to_NP(one_to_NP~=j);
    end

    % init solution
    x = lim(1) + rand(NP, dim) * (lim(2)-lim(1));
    y = zeros(NP, dim);  % trial vectors
    fx = func(x);
    fval_hist = [];
    
    for iter = 1:max_iter
        [~, best_idx] = min(fx);
        fval = fx(best_idx);
        x_out = x(best_idx);
        fprintf('fval: %f\n', fval);
        % add fval to history of maximum length
        if length(fval_hist) == max_iter_eps
            fval_hist = [fval_hist(2:end), fval];
            max_diff = max(abs(diff(fval_hist)));
            if max_diff < epsilon
                break;  % terminate condition
            end
        else
            fval_hist = [fval_hist, fval];
        end
        % random numbers for crossover generated ahead
        r = rand(NP, dim);
        R = randi([1, dim], NP, 1);
        y(:, :) = x(:, :);  % copy values, overwrite only when crossover
        for j = 1:NP
            idx = randsample(choices_cache(j, :), 3);
            a = x(idx(1), :);
            b = x(idx(2), :);
            c = x(idx(3), :);
            d = a + F * (b - c);
            for i=1:dim
                if i == R(j) || r(j, i) < CR  % cossover
                    if lim(1) <= d(i) && lim(2) <= d(i)
                        y(j, i) = d(i);
                    else
                        y(j, i) = lim(1) + rand() * (lim(2)-lim(1));
                    end
                end
            end
        end
        fy = func(y);
        is_better = fy < fx;
        x(is_better, :) = y(is_better, :);
        fx(is_better) = fy(is_better);
    end
    
    fprintf("terminated after iteration %i\n", iter);
    
end
