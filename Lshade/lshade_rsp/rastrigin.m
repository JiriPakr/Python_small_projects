function [z] = rastrigin(x1, y1)
    A = 10;
    x = [x1,y1];
    n = size(x, 2);
    z = A*n + sum(x.^2 - A*cos(2*pi*x), 2);
end