# Generate multiplication tables and write them to separate files
# for i in range(1, 21):
#     with open(f"tables/multi_{i}.txt", "w") as f:
#         for e in range(1, 11):
#             st = f"{i} X {e} = {i * e}\n"
#             f.write(st)

for i in range(1,21):
    with open(f"tables/multi_{i}.txt", "w") as f:
        for e in range(1,11):
            st = f"{i} X {e} = {i*e}\n"
            f.write(str(st))