
# ========================= Modules 

import module

from module import i_am_method, Module



print(module.i_am_method())

print(i_am_method())


print(module.Module.say_hi())

print(Module.say_hi())


# ================================ Modules/Packages


import package
from package.pack_mod import PackageModule
# from package.pack_mod.PackageModule import say_hi

print(package.pack_mod.PackageModule.say_hi())

print(PackageModule.say_hi())

# print(say_hi())
