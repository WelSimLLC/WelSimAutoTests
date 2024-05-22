# WelSimAutoTests
This repository contains official WelSim regression test cases. You are welcome to run the tests on your local computer or submit new test cases.

![WELSIM regression GUI](https://github.com/WelSimLLC/WelSimAutoTests/blob/main/98_Gallery/welsim_regression_system_playback_ui_clean.png)

## Running tests
1. Download the zip file or clone the repository.
2. Set environment variables **WELSIM_DATA_ROOT** to the **WelSimAutoTests** folder.
3. Start the WELSIM application, select the **Play test...** action from the menu **Tools**.
4. Load the test cases and run.

> [!IMPORTANT]
> All test cases are synchronized with the latest development version. Please run the test cases using the latest development version of WELSIM. 

> [!IMPORTANT]
> The user needs to configure the **OpenRadioss**, **CalculiX**, and **Elmer** solvers by first before running the specific test cases. 


## Creating tests
1. Set environment variables WELSIM_DATA_ROOT to the external file folder.
2. Start the WELSIM application, and select the **Record test...** action from the menu **Tools**.
3. Record operation flow.
4. Manually revise the test case if necessary. 



## Statistics
| **Folder** | **Number of Tests** | **External Solver** |
|------------|---------------------|-----------|
| 04_GUI | 28 | - [ ] |
| 06_MatEditor | 153 | - [ ] |
| 07_Mesh | 12 | - [ ] |
| 08_Result | 8 | - [ ] |
| 09_BeamSection | 8 | - [ ] |
| 11_FrontISTR | 38 | - [] |
| 12_OpenRadioss | 7 | - [x] |
| 13_CalculiX | 8 | - [x] |
| 14_Elmer | 12 | - [x] |
| 21_SU2 | 3 | - [ ] |
| 32_Palace | 2 | - [ ] |
| **Total** | **279** |

