from keras.models import Model
from keras.layers import LSTM
from keras.callbacks import LearningRateScheduler

def scheduler(epoch):
    if epoch < nb_epochs/4:
        return learning_rate
    elif epoch < nb_epochs/2:
        return learning_rate*0.5
    return learning_rate*0.1


f = open("data.pkl", 'rb')
X,Y = cPickle.load(f)

hidden_size = 512
seq_len = 11
nb_epochs = 100
learning_rate = 0.1

main_input = Input(shape=(seq_len, 2), name='main_input')

encoder = LSTM(output_dim = hidden_size, return_sequences = True, name="encoder")(main_input)
decoder = PointerLSTM(hidden_size, output_dim = hidden_size, name="decoder")(encoder)

model = Model(input=main_input, output=decoder)
model.compile(optimizer='adadelta',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

model.fit(X,Y, nb_epoch=nb_epochs, batch_size=8000,callbacks=[LearningRateScheduler(scheduler),])
model.save_weights('model_weight_100.hdf5')
