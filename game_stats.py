

class GameStats():
	#游戏信息统计
	
	def __init__(self,ai_settings):
		"""初始化"""
		self.ai_settings=ai_settings
		self.reset_stats()

		self.game_active = False

	def reset_stats(self):
		#船的数量
		self.ships_left = self.ai_settings.ship_limit
