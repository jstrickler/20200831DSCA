company = "Apple"
product = 'iPad'
result = 24.19 / 7.86

print(company, product, result)

print(company, product, result, sep='/')
print(company, product, result, sep=', ')
print(company, sep="/")
print()

print(company)
print(product)
print(result)
print()

print(company, end="--")
print(product, end="//")
print(result)

print(company, product, result, sep="SEP", end="END")
print("\n")

print("The", product, "is made by", company)
print("The {} is made by {}".format(product, company))
print("The {} is made by {}".format(company, product))

print(f"The {product} is made by {company}")

print(f"The result is {result}")
print(f"The result is {result:.3f}")
print("The result is {:.3f}".format(result))
