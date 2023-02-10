function [z] = schaffer(x,y)
    n=length(x);
    for i = 1:n
        z(i) = 0.5 + ((sin(x(i)^2-y(i)^2)^2)-0.5)/((1+0.001*(x(i)^2+y(i)^2))^2);
    end
end