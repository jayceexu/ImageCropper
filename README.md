# ImageCropper
1. Capturing XML DOM tree of current UI displayed on screen from mobile/wearable devices
2. Capturing UI PNG file of current UI

   Caution: while capturing, please wait 5 second for each UI as each capturing procedure takes 5 seconds.
3. Splitting each UI PNG image into parts, based on the XML DOM tree description

## Tutorial

### On the mobile/wearable side
#### Deploying on mobile/wearable devices
```
adb push scrap.sh /sdcard/
adb shell
cd /sdcard/
mkdir uiCaps
mv /sdcard/scrap.sh /sdcard/uiCaps/
```

#### Running script
```
adb shell 
cd /sdcard/uiCaps/
sh scrap.sh
```

### On the desktop side
#### Grabbing content from the device
```
adb pull /sdcard/uiCaps/  .
```
#### Parsing the XML and Splitting UI PNGs
```
cp ~/parse.py uiCaps/
cd uiCaps/
python parse.py
```
