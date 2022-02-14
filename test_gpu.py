import torch
flag = torch.cuda.is_available()

if flag:
    print("CUDA Ok")
else:
    print("CUDA Failed")
ngpu = 1
device = torch.device("cuda:0" if (torch.cuda.is_available() and ngpu > 0) else "cpu")
print("驱动为: ", device)
print("GPU型号： ", torch.cuda.get_device_name(0))
