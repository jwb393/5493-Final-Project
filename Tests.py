from unittest.mock import patch
from FinalProjectElectricalTool import get_float_input, ohms_law_menu, power_menu, capacitance_menu


class TestGetFloatInput:
    @patch('builtins.input')
    def test_valid_input(self, mock_input):
        mock_input.return_value = '5.5'
        result = get_float_input("Enter value: ")
        assert result == 5.5

    @patch('builtins.input')
    @patch('builtins.print')
    def test_negative_input_retry(self, mock_print, mock_input):
        mock_input.side_effect = ['-1', '3.0']
        result = get_float_input("Enter value: ")
        assert result == 3.0
        assert mock_print.call_count == 1
        mock_print.assert_called_with("Error: Value must be non-negative. Try again.")

    @patch('builtins.input')
    @patch('builtins.print')
    def test_invalid_input_retry(self, mock_print, mock_input):
        mock_input.side_effect = ['abc', '2.5']
        result = get_float_input("Enter value: ")
        assert result == 2.5
        assert mock_print.call_count == 1
        mock_print.assert_called_with("Error: Invalid input. Please enter a valid number.")


class TestOhmsLawMenu:
    @patch('builtins.input')
    @patch('builtins.print')
    def test_calculate_voltage(self, mock_print, mock_input):
        mock_input.side_effect = ['1', '2.0', '10.0']
        ohms_law_menu()
        # Check that voltage calculation was printed
        calls = [call.args[0] for call in mock_print.call_args_list]
        assert "Voltage: 20.00 V" in calls

    @patch('builtins.input')
    @patch('builtins.print')
    def test_calculate_current(self, mock_print, mock_input):
        mock_input.side_effect = ['2', '20.0', '10.0']
        ohms_law_menu()
        calls = [call.args[0] for call in mock_print.call_args_list]
        assert "Current: 2.00 A" in calls

    @patch('builtins.input')
    @patch('builtins.print')
    def test_calculate_resistance(self, mock_print, mock_input):
        mock_input.side_effect = ['3', '20.0', '2.0']
        ohms_law_menu()
        calls = [call.args[0] for call in mock_print.call_args_list]
        assert "Resistance: 10.00 Ω" in calls

    @patch('builtins.input')
    @patch('builtins.print')
    def test_zero_resistance_voltage(self, mock_print, mock_input):
        mock_input.side_effect = ['1', '2.0', '0']
        ohms_law_menu()
        calls = [call.args[0] for call in mock_print.call_args_list]
        assert "Error: Resistance cannot be zero." in calls

    @patch('builtins.input')
    @patch('builtins.print')
    def test_zero_resistance_current(self, mock_print, mock_input):
        mock_input.side_effect = ['2', '20.0', '0']
        ohms_law_menu()
        calls = [call.args[0] for call in mock_print.call_args_list]
        assert "Error: Resistance cannot be zero." in calls

    @patch('builtins.input')
    @patch('builtins.print')
    def test_zero_current_resistance(self, mock_print, mock_input):
        mock_input.side_effect = ['3', '20.0', '0']
        ohms_law_menu()
        calls = [call.args[0] for call in mock_print.call_args_list]
        assert "Error: Current cannot be zero." in calls

    @patch('builtins.input')
    @patch('builtins.print')
    def test_invalid_choice(self, mock_print, mock_input):
        mock_input.return_value = '5'
        ohms_law_menu()
        calls = [call.args[0] for call in mock_print.call_args_list]
        assert "Error: Invalid selection." in calls


class TestPowerMenu:
    @patch('builtins.input')
    @patch('builtins.print')
    def test_calculate_power_vi(self, mock_print, mock_input):
        mock_input.side_effect = ['1', '10.0', '2.0']
        power_menu()
        calls = [call.args[0] for call in mock_print.call_args_list]
        assert "Power: 20.00 W" in calls

    @patch('builtins.input')
    @patch('builtins.print')
    def test_calculate_power_ir(self, mock_print, mock_input):
        mock_input.side_effect = ['2', '2.0', '5.0']
        power_menu()
        calls = [call.args[0] for call in mock_print.call_args_list]
        assert "Power: 20.00 W" in calls

    @patch('builtins.input')
    @patch('builtins.print')
    def test_calculate_voltage(self, mock_print, mock_input):
        mock_input.side_effect = ['3', '20.0', '2.0']
        power_menu()
        calls = [call.args[0] for call in mock_print.call_args_list]
        assert "Voltage: 10.00 V" in calls

    @patch('builtins.input')
    @patch('builtins.print')
    def test_calculate_current(self, mock_print, mock_input):
        mock_input.side_effect = ['4', '20.0', '10.0']
        power_menu()
        calls = [call.args[0] for call in mock_print.call_args_list]
        assert "Current: 2.00 A" in calls

    @patch('builtins.input')
    @patch('builtins.print')
    def test_zero_current_voltage(self, mock_print, mock_input):
        mock_input.side_effect = ['3', '20.0', '0']
        power_menu()
        calls = [call.args[0] for call in mock_print.call_args_list]
        assert "Error: Current cannot be zero." in calls

    @patch('builtins.input')
    @patch('builtins.print')
    def test_zero_voltage_current(self, mock_print, mock_input):
        mock_input.side_effect = ['4', '20.0', '0']
        power_menu()
        calls = [call.args[0] for call in mock_print.call_args_list]
        assert "Error: Voltage cannot be zero." in calls

    @patch('builtins.input')
    @patch('builtins.print')
    def test_invalid_choice(self, mock_print, mock_input):
        mock_input.return_value = '5'
        power_menu()
        calls = [call.args[0] for call in mock_print.call_args_list]
        assert "Error: Invalid selection." in calls


class TestCapacitanceResistanceMenu:
    @patch('builtins.input')
    @patch('builtins.print')
    def test_menu_capacitance_series(self, mock_print, mock_input):
        mock_input.side_effect = ['1', '2.0, 3.0, 6.0']
        capacitance_menu()
        calls = [call.args[0] for call in mock_print.call_args_list]
        assert "Total Capacitance in Series: 1.00e+00 F" in calls

    @patch('builtins.input')
    @patch('builtins.print')
    def test_menu_capacitance_parallel(self, mock_print, mock_input):
        mock_input.side_effect = ['2', '2.0, 3.0, 6.0']
        capacitance_menu()
        calls = [call.args[0] for call in mock_print.call_args_list]
        assert "Total Capacitance in Parallel: 1.10e+01 F" in calls

    @patch('builtins.input')
    @patch('builtins.print')
    def test_menu_resistance_series(self, mock_print, mock_input):
        mock_input.side_effect = ['3', '5.0, 10.0']
        capacitance_menu()
        calls = [call.args[0] for call in mock_print.call_args_list]
        assert "Total Resistance in Series: 15.00 Ω" in calls

    @patch('builtins.input')
    @patch('builtins.print')
    def test_menu_resistance_parallel(self, mock_print, mock_input):
        mock_input.side_effect = ['4', '5.0, 10.0']
        capacitance_menu()
        calls = [call.args[0] for call in mock_print.call_args_list]
        assert "Total Resistance in Parallel: 3.33 Ω" in calls

    @patch('builtins.input')
    @patch('builtins.print')
    def test_menu_invalid_selection(self, mock_print, mock_input):
        mock_input.return_value = '9'
        capacitance_menu()
        calls = [call.args[0] for call in mock_print.call_args_list]
        assert "Error: Invalid selection." in calls
