# tracking-demo
Object tracking demo with hardware PID response

## pseudocode
```
init KCF and MedianFlow
store ROI image (confidence = 1; max confidence = 1)

while(True):
	get frame
	if no tracking failures:
		if a ROI image matches a region in the frame:
			exert influence on both trackers (average?) with identified region
			increase the confidence in the stored image
				(ex: confidence = 0.5 + 0.5*confidence)
		else:
			store a picture of the ROI (confidence = 0.5*confidence of previous match*(something that decreases over time)))
	if one tracking failure:
		if a ROI image matches with a region in the frame close to the
		tracker that didn't fail:
			exert influence on the working tracker's ROI
			reinitialize the other tracker with the the working tracker's ROI
		if a ROI image doesn't match:
			only update the working tracker; do not reinitialize
	if two tracking failures:
		continue on current settings
		try to match a stored image with the frame
		if match:
			reinitialize both trackers to the stored image

	confidence should decrease after the passage of time without a match
```