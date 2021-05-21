# neural-style -style_image /Users/egor.nakonechnyyicloud.com/PycharmProjects/MEETKEYmain/main/masks/VanGOG.jpeg -content_image /Users/egor.nakonechnyyicloud.com/PycharmProjects/MEETKEYmain/testsuff/me.jpg -output_image profile.png -model_file /Users/egor.nakonechnyyicloud.com/vgg19-d01eb7cb.pth -gpu 0 -backend cudnn -num_iterations 1000 -seed 123 -content_layers relu0,relu3,relu7,relu12 -style_layers relu0,relu3,relu7,relu12 -content_weight 10 -style_weight 500 -image_size 512 -optimizer adam
# neural-style -style_image /Users/egor.nakonechnyyicloud.com/PycharmProjects/MEETKEYmain/main/masks/VanGOG.jpeg -content_image /Users/egor.nakonechnyyicloud.com/PycharmProjects/MEETKEYmain/testsuff/me.jpg -model_file /Users/egor.nakonechnyyicloud.com/vgg19-d01eb7cb.pth
import pyaudio
p = pyaudio.PyAudio()
for i in range(p.get_device_count()):
    print(p.get_device_info_by_index(i))

