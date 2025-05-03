from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Conv2D, BatchNormalization, ReLU, MaxPooling2D, Flatten, Dense

def Meso4():
    x = Input(shape=(256, 256, 3))

    y = Conv2D(8, (3, 3), padding='same')(x)
    y = BatchNormalization()(y)
    y = ReLU()(y)
    y = MaxPooling2D(pool_size=(2, 2))(y)

    y = Conv2D(8, (5, 5), padding='same')(y)
    y = BatchNormalization()(y)
    y = ReLU()(y)
    y = MaxPooling2D(pool_size=(2, 2))(y)

    y = Conv2D(16, (5, 5), padding='same')(y)
    y = BatchNormalization()(y)
    y = ReLU()(y)
    y = MaxPooling2D(pool_size=(2, 2))(y)

    y = Conv2D(16, (5, 5), padding='same')(y)
    y = BatchNormalization()(y)
    y = ReLU()(y)
    y = MaxPooling2D(pool_size=(4, 4))(y)

    y = Flatten()(y)
    y = Dense(16)(y)
    y = ReLU()(y)
    y = Dense(1, activation='sigmoid')(y)

    return Model(inputs=x, outputs=y)
