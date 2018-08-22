import os, time, tcfl.tc
@tcfl.tc.target('zephyr_board', app_zephyr = os.path.join("."))
class _test(tcfl.tc.tc_c):
    def setup_catch_failures(self, target):
        target.on_console_rx("FAIL", result = 'fail', timeout = False)

    def eval(self, target):
        target.expect("PASS")
