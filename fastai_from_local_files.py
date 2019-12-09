from fastai.vision import *
from google.colab import drive
drive.mount('/content/drive')

path = Path('/content/drive/My Drive/fastai_classification')

"""create the different csv files give them each the right folder name """

for file, folder in [('csv_f16.csv', 'f16'), ('csv_f22.csv', 'f22'), 
                     ('csv_f35.csv', 'f35')]:
    dest = path/'jets'/folder # path + '/' + folder
    dest.mkdir(parents=True, exist_ok=True)
    download_images(path/file, dest)

"""give overview of what is in the folders now"""

from os import listdir
jet_images_folder_path = path/'jets'
print(os.listdir(path))
print(os.listdir(jet_images_folder_path))
print(os.listdir(jet_images_folder_path/'f16')[:10])

""" filter out the images that are not usable thanks to filter tool by fastai"""

for folder in ('f22', 'f35', 'f16'):
    print(folder)
    verify_images(jet_images_folder_path/folder, delete=True, max_size=500)

"""
create the image databunch for fastai
We now have changed the value of size to (224,224) instead of 224. This change, although not obvious, squishes the image to the same dimensions mentioned:
"""

data = ImageDataBunch.from_folder(jet_images_folder_path
                                  , ds_tfms=get_transforms()
                                  , size=(224,224)
                                  , valid_pct=0.2
                                 ).normalize()

"""verify the classes show some pictures"""

print(data.classes)
data.show_batch(rows=3, figsize=(7, 8))

"""How many pics do we have?"""

print(data.train_ds, '\n')
print(data.valid_ds)

"""create our resnet model with metric error rate"""

from fastai.metrics import error_rate # 1 - accuracy
learn = cnn_learner(data, models.resnet34, metrics=error_rate)

"""train the model the first time save this"""

learn.fit_one_cycle(4, 1e-2)
learn.save('stage_1')

"""find a better learning rate"""

learn.lr_find()
learn.recorder.plot(suggestion=True)
# 0.00831636352 #9.12E-07
# 0.28627564311 #5.75E-03


"""train the model again with the updated learning right now unfreeze it to also train the body"""
"""we use the slice method to gradually increase learning rates on different layers"""

learn.lr_find()
learn.recorder.plot(suggestion=True)

learn.load('stage_1')
learn.unfreeze() # better performance without unfreezing why ?
learn.fit_one_cycle(4, max_lr=slice(9.12e-07, 5.75e-03))
learn.save('stage_2')

"""create interpreter for our model show the pictures it had difficulties with"""

learn.load('stage_2')
interp = ClassificationInterpretation.from_learner(learn)
interp.plot_top_losses(9, figsize=(15,15))

interp.most_confused(min_val=2)

"""show the confusion matrix in raw numbers but also normalized"""

interp.plot_confusion_matrix()

interp.plot_confusion_matrix(normalize=True)