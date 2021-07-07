samples = samples/

[samples]
# list your samples here
kick7 = biab_kick_7.wav
snare2 = biab_sn_2.wav
snare10 = biab_sn_10.wav
hihat2 = biab_hat_2.wav
hihat4 = biab_hat_4.wav

[song]
# basic song parameters and pattern sequence
bpm = 128
ticks = 4
patterns = pat1 pat2 pat1 pat2 outro

[pattern.pat1]
hihat2     = x.x. x.x. x.x. x.x.
snare2     = .... x... .... x...
kick7      = x... x... x... x...

[pattern.pat2]
hihat4     = x.x. x.x. x.x. x.x.
snare10    = .... .... x... x...

[pattern.outro]
hihat2     = x.x. x.x. 
hihat4     = .... x...
kick7      = .... x...

