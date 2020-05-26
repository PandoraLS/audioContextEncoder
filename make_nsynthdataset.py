from datasetGenerator.exampleProcessor import ExampleProcessor
from datasetGenerator.nSynthDownloader import NSynthDownloader
from datasetGenerator.nSynthTFRecordGenerator import NSynthTFRecordGenerator
import os
__author__ = 'Andres'


# downloader = NSynthDownloader()
# downloader.downloadAndExtract()
root = "/home/lisen/uestc/TX/code/audioContextEncoder/datasetGenerator/nysnth-valid-demo"
TRAIN_DIR = os.path.join(root, "train-audio")
VALID_DIR = os.path.join(root, "valid-audio")
TEST_DIR = os.path.join(root, "test-audio")

exampleProcessor = ExampleProcessor(gapLength=1024, sideLength=2048, hopSize=512, gapMinRMS=1e-3)

tfRecordGenerator = NSynthTFRecordGenerator(baseName='nsynth_test', pathToDataFolder=TEST_DIR, exampleProcessor=exampleProcessor)
tfRecordGenerator.generateDataset()

tfRecordGenerator = NSynthTFRecordGenerator(baseName='nsynth_valid', pathToDataFolder=VALID_DIR, exampleProcessor=exampleProcessor)
tfRecordGenerator.generateDataset()

tfRecordGenerator = NSynthTFRecordGenerator(baseName='nsynth_train', pathToDataFolder=TRAIN_DIR, exampleProcessor=exampleProcessor)
tfRecordGenerator.generateDataset()
