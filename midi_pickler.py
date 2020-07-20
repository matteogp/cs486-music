import matplotlib
import scipy
from music21 import converter, instrument, note, chord, stream
import numpy
import glob
import keras.utils.np_utils as np_utils
import pickle

genre = 'edm'

def load_notes(genre):
    notes = []
    i = 0
    file_list = glob.glob(genre+"*.mid")
    for file in file_list:
        print(i, file)
        midi = converter.parse(file)
        print('parsed')
        notes_to_parse = None
        parts = instrument.partitionByInstrument(midi)
        print(parts)
        if parts: # file has instrument parts
            notes_to_parse = parts.parts[0].recurse()
        else: # file has notes in a flat structure
            notes_to_parse = midi.flat.notes
        for element in notes_to_parse:
            if isinstance(element, note.Note):
                notes.append(str(element.pitch))
            elif isinstance(element, chord.Chord):
                notes.append('.'.join(str(n) for n in element.normalOrder))
        i += 1

    return notes, file_list


notes_file, files_noted = load_notes(f'{genre}/')
pickle_out = open(f"{genre}_notes.pickle", "wb")
pickle.dump(notes_file, pickle_out)
print(files_noted)
