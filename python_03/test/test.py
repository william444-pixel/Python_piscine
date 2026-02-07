import sys

# هادي كتعمر الميموري
def get_list(n):
    result = []
    for i in range(n):
        result.append(i)
    return result

# هادي هي الـ Generator ديالك
def streaming_info(n):
    for i in range(n):
        yield i

# نختبروا بمليون عنصر
n = 1000000
big_list = get_list(n)
gen_obj = streaming_info(n)

print(f"List size: {big_list} bytes")
print(f"Generator size: {next(gen_obj)}  bytes")
