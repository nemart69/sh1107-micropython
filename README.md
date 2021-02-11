# sh1107-micropython
Micropython driver for SH1107-based OLED display (64 x 128)

Driver with the same API as micropython built-in SSD1306 driver:
* I2C only
* Tested with https://www.aliexpress.com/item/4000464960639.html; both in 128 x 64 and 64 x 128 pixels mode
* Not tested in 128 x 128 pixel mode
* Implements simple optimization to reduce the amount of data sent during show() 
