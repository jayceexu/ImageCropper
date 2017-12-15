# ImageCropper
1. Capturing XML DOM tree of current UI displayed on screen from mobile/wearable devices
2. Capturing UI PNG file of current UI
3. Splitting each UI PNG image into parts, based on the XML DOM tree description

## Tutorial

### Deploying on mobile/wearable devices
```
adb push scrap.sh /sdcard/
adb shell
cd /sdcard/
mkdir uiCaps
mv /sdcard/scrap.sh /sdcard/uiCaps/
```

### Running script on the device
```
adb shell 
cd /sdcard/uiCaps/
sh scrap.sh
```

### Grabbing content from the device on the desktop
```
mkdir exp
# Copy parse.py into the 'exp' directory
cd exp
adb pull /sdcard/uiCaps/  .

```
### Parsing the XML and Splitting UI PNGs
```
cp ~/parse.py uiCaps/
cd uiCaps/
python parse.py
```
