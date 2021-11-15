#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Stochastic Weight Averaging: https://arxiv.org/abs/1803.05407
Implementaton in Keras from user defined epochs assuming constant
learning rate
Cyclic learning rate implementation in https://arxiv.org/abs/1803.05407
not implemented
Created on July 4, 2018
@author: Krist Papadopoulos
"""

import keras


class SWA(keras.callbacks.Callback):
    def __init__(self, filepath, swa_epoch):
        super(SWA, self).__init__()
        self.filepath = filepath
        self.swa_epoch = swa_epoch

    def on_train_begin(self, logs=None):
        self.nb_epoch = self.params["epochs"]
        print(
            "Stochastic weight averaging selected for last {} epochs.".format(
                self.nb_epoch - self.swa_epoch
            )
        )

    def on_epoch_end(self, epoch, logs=None):

        if epoch == self.swa_epoch:
            self.swa_weights = self.model.get_weights()

        elif epoch > self.swa_epoch:
            for i, layer in enumerate(self.model.layers):
                self.swa_weights[i] = (
                    self.swa_weights[i] * (epoch - self.swa_epoch)
                    + self.model.get_weights()[i]
                ) / ((epoch - self.swa_epoch) + 1)

        else:
            pass

    def on_train_end(self, logs=None):
        self.model.set_weights(self.swa_weights)
        print("Final model parameters set to stochastic weight average.")
        self.model.save_weights(self.filepath)
        print("Final stochastic averaged weights saved to file.")


from keras.callbacks import Callback
import keras.backend as K
import signal
import time


class KeyboardLRDrop(Callback):
    """Stop training when an interrupt signal (or other) was received
            # Arguments
            sig: the signal to listen to. Defaults to signal.SIGINT.
            doubleSignalExits: Receiving the signal twice exits the python
                    process instead of waiting for this epoch to finish.
            patience: number of epochs with no improvement
                    after which training will be stopped.
            verbose: verbosity mode.
    """

    # SBW 2018.10.15 Since ctrl-c trapping isn't working, watch for existence of file, e.g. .\path\_StopTraining.txt.

    def __init__(
        self, sig=signal.SIGINT, doubleSignalExits=True, factor=0.1, verbose=1
    ):
        super(KeyboardLRDrop, self).__init__()
        self.signal_received = False
        self.verbose = verbose
        self.doubleSignalExits = doubleSignalExits

        def signal_handler(sig, frame):
            if self.signal_received and self.doubleSignalExits:
                if self.verbose > 0:
                    # new line to not print on current status bar. Better solution?
                    print("")
                    print(("Received signal to stop " + str(sig) + " twice. Exiting.."))
                raise KeyboardInterrupt
            self.signal_received = True
            if self.verbose > 0:
                # new line to not print on current status bar. Better solution?
                print("")
                print(("Received signal to stop: " + str(sig)))
                old_lr = float(K.get_value(self.model.optimizer.lr))
                new_lr = old_lr * factor
                print(f"Learning rate was {old_lr}, now it is {new_lr}")
                K.set_value(self.model.optimizer.lr, new_lr)

        signal.signal(signal.SIGINT, signal_handler)
        self.stopped_epoch = 0

    def on_epoch_end(self, epoch, logs={}):
        self.signal_received = False
        # SBW 2018.10.15 Since ctrl-c trapping isn't working, watch for existence of file, e.g. .\path\_StopTraining.txt.
