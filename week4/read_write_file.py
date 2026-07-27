with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)


#for images
# with open('test.txt', 'rb') as rf:
#     with open('test_copy.txt', 'wb') as wf:
#         for line in rf:
#             wf.write(line)

