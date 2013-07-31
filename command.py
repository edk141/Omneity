from org.bukkit.command import Command
from org.bukkit import Bukkit
from org.bukkit.plugin import SimplePluginManager
from org.bukkit.command import Command


_commandmap_field = SimplePluginManager.getDeclaredField("commandMap")
_commandmap_field.setAccessible(True)
commandmap = _commandmap_field.get(Bukkit.getPluginManager())


class PythonCommand(Command):

	def __init__(self, func, name, description, usage, aliases, tab_complete):
		super(Command, self).__init__(name, description, usage, aliases)
		self.func = func
		self.tab_complete = tab_complete
	
	def execute(self, sender, label, args):
		self.func(sender, label, args)

	def tabComplete(self, sender, alias, args):
		if self.tab_complete:
			self.tab_complete(sender, alias, args)


def register_command(func, command_name, tab_complete=None, description="", usage="/<command>", permission=None, aliases=[]):
	command = PythonCommand(func, command_name, description, usage, aliases, tab_complete)
	command.setPermission(permission)
	commandmap.register("/", command)