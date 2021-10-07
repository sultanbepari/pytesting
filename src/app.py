import pandas as pd
from PIL import Image
import glob


def csv2json():
    df = pd.read_csv (r'src/csv2json/Name.csv')
    df.to_json (r'src/csv2json/JSON.js')
    return 0


def jpg2gif():
    frame_folder = r'src/jpg_to_gif/images'
    frames = [Image.open(image) for image in glob.glob(f"{frame_folder}/*.jpg")]
    frame_one = frames[0]
    frame_one.save("src/jpg_to_gif/my_awesome.gif", format="GIF", append_images=frames,
                   save_all=True, duration=100, loop=0)

    return 0



if __name__ == "__main__":
    app.run()




