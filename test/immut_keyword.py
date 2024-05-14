def immut_example():
    immut str # type: ignore
    str = "Hello, World!" # type: ignore
    print(str)

immut_example()

# Frozen frozen_var = "Hello, World!"
# frozen_var: Frozen[str] = "Hello, World!"
