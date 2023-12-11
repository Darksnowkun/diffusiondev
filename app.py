from diffusers import StableDiffusionPipeline
import os
from dotenv import load_dotenv

def setup():
    load_dotenv()
    token=os.getenv('HUG_TOKEN')
    return token

url = ""
pipeline = StableDiffusionPipeline.from_single_file(url)
print(setup())
