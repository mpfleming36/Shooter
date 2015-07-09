# CS391GameInfrastructure
Shooter Game
Mike Fleming
SIU851207239

Objective:
	+Kill all the enemies without dying

Difficulty:
	+1 - Enemies have no health multiplier
	+2 - Enemies have a 2x health multiplier
	+3 - Enemies have a 3x health multiplier

Controls-
	+W - Up
	+S - Down
	+A - Left
	+D - Right
	+Space - Shoot
	+E - Change Weapons
	+1 - Choose Shotgun
	+2 - Choose SMG
	+3 - Choose Rockets

Known Bugs:
	+Bullets Collisionbox remain when they hit something
		-After hitting enemies
		-After hidding bounds
	+Previous gunOrigin and facing remain after restart
		-Causes a new ghost gun after each restart
		-Updates when player shoots and changes gun
	+When pressing E to change weapons
		-There is no delay between presses
		-Not accurate for changing to next weapon
		-Creates "Supergun" when holding (fun glitch so didn't put in instructions)