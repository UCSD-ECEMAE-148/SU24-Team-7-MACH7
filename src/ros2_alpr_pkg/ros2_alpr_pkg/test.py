from openalpr import Alpr
from argparse import ArgumentParser
import pandas as pd

def recognize_plate(image_path, country="us", config="/home/projects/openalpr/config/openalpr.conf.defaults", runtime_data="/home/projects/openalpr/runtime_data"):
    alpr = None
    recognized_plates = []
    try:
        alpr = Alpr(country, config, runtime_data)

        if not alpr.is_loaded():
            print("Error loading OpenALPR")
        else:
           # print("Using OpenALPR " + alpr.get_version())


            alpr.set_top_n(7)
            alpr.set_default_region("wa")
            alpr.set_detect_region(False)
            jpeg_bytes = open(image_path, "rb").read()
            results = alpr.recognize_array(jpeg_bytes)

        # Uncomment to see the full results structure
        # import print
        # pprint.pprint(results)




            i = 0
            for plate in results['results']:
                i += 1
               # print("Plate #%d" % i)

                if plate['candidates']:
                    candidate = plate['candidates'][0]
                    recognized_plates.append(candidate['plate'])
                    prefix = "-"
                if candidate['matches_template']:
                    prefix = "*"
                print("   %12s" % (candidate['plate']))


    finally:
        if alpr:
            alpr.unload()
    return recognized_plates
