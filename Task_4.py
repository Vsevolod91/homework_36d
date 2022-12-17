class Meta(type):
    def __new__(cls, name, bases, attrs):
        mod_attrs = {}
        count_it = 0
        for a in attrs:
            count_it += 1
            if count_it <= 2:
                mod_attrs[a] = attrs[a]
            else:
                n = a.upper()
                mod_attrs[n] = attrs[a]
        return type.__new__(cls, name, bases, mod_attrs)


class Math(metaclass=Meta):
    pi = 3.141592653589793
    e = 2.718281828459045
    tau = 6.283185307179586

m = Math()
print(m.PI)
print(m.E)
print(m.pi)