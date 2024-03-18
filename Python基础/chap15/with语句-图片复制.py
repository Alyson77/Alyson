with open('c.jpg','rb') as src_file:
    with open('copy2.jpg','wb') as target_file:
        target_file.write(src_file.read())