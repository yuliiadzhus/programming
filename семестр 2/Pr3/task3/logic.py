def copy_file(name):
    with open(name, "rb") as f_in, open("copy_" + name, "wb") as f_out:
        f_out.write(f_in.read())