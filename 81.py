# ************************  Hybrid and Hierarchical Inheritance  ************************

# Hybrid Inheritance : The process of combining more than one type of Inheritance together while deriving subclasses in a program is called a Hybrid Inheritance.

# e.g. (combination of heirarchical and multilevel inheritance)

#                 A
#              /     \
#             B       C
#              \     /
#                 D

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass


# Hierarchical Inheritance : When more than one class is inherited from a single base class.

# e.g.

#                 E
#              /  |  \
#             F   G   H

class E:
    pass

class F(E):
    pass

class G(E):
    pass

class H(E):
    pass
