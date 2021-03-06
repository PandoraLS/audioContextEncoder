import pickle

from architecture.contextEncoderArchitecture import ContextEncoderArchitecture
from system.contextEncoderSystem import ContextEncoderSystem
from system.preAndPostProcessor import PreAndPostProcessor

architecturesParametersFile = "complex_network_parameters.pkl"
sessionsName = "complex_network"

with open(architecturesParametersFile, 'rb') as savedFile:
    Context_Encoder_parameters = pickle.load(savedFile)

aContextEncoderArchitecture = ContextEncoderArchitecture(*Context_Encoder_parameters.architectureParameters())
aPreProcessor = PreAndPostProcessor(*Context_Encoder_parameters.preProcessorParameters())
aContextEncoderSystem = ContextEncoderSystem(aContextEncoderArchitecture, Context_Encoder_parameters.batchSize(),
                                             aPreProcessor, sessionsName)
aContextEncoderSystem.train("nsynth_train_w5120_g1024_h512.tfrecords", "nsynth_valid_w5120_g1024_h512.tfrecords", 1e-3)
