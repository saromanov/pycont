# PyCont

Very basic containers with ```debootstrap``` and ```chroot```

# Usage

Download base system
```python
container = PyCont('/container') #Create container to the path /container
container.get() #Download default system. debootstrap wheezy http://http.debian.net/debian/
```

Run command
```python
container = pycont.PyCont('/container')
container.execute('/bin/ls', arg=['-la'])
container.umount()
```

# LICENE
MIT @saromanov
