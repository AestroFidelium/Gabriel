from PIL import Image, ImageDraw , ImageFont
import os

def ReadImage(ImageName : str):
    Expansion = str(ImageName).split(".")[-1]
    NameFile = str(ImageName).split(".")[0]

    image = Image.open(f"./Coordinator/{ImageName}")
    image.save(f"./Coordinator/{NameFile} (Edited).{Expansion}")
    image.show()

def main():
    print("START")
    directory = "./Coordinator/"
    # Photo = Image.open("photo_name.png")
    files = os.listdir(directory)
    for file in files:
        if file != "Coordinate.py":
            ReadImage(file)


if __name__ == "__main__":
    main()
    print("END")
    pass