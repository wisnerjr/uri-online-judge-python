product_1_code, product_1_count, product_1_price = input().split()
product_2_code, product_2_count, product_2_price = input().split()


total = ((int(product_1_count) * float(product_1_price)) +
         (int(product_2_count) * float(product_2_price)))


print("VALOR A PAGAR: R$ %0.2f" % total)
