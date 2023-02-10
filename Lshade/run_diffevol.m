
% Octave needs for randsample:  pkg install -forge io statistics

% Octave compatibility, pakage load
isOctave = exist('OCTAVE_VERSION', 'builtin') ~= 0;
if isOctave
    pkg load statistics
end

rastrigin_A10 = @(x) rastrigin(x, 10);

dim=2;   lim=[-5.12, 5.12];
NP=100;
F=0.2;  CR=0.7;
max_iter=1000;  max_iter_eps=10;   epsilon=1e-9;

[x_out, fval] = diffevol(rastrigin_A10, dim, lim, NP, F, CR, max_iter, max_iter_eps, epsilon);
fprintf('found solution:');
fprintf('    x: %s\n fval: %f\n', mat2str(x_out), fval);
