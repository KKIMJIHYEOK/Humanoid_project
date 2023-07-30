라즈베리파이에서 재부팅시 프로그램을 자동시작 하는 방법 2가지 

1. 윈도우 창이 있는 프로그램 실행 하는 방법(꼭 부팅시 DeskTop 모드 부팅해야 함) 

	이 방법의 장점은 startx까지 모두 실행한후에 실행하므로 대부분의 GUI프로그램들이 잘 작동한다는 점이다.
	
	터미널에서 다음파일을 연다.
	sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
	
	여기서 맨 아래 @xscreensaver 밑으로 아래 명령어과 같은 3가지 방법으로 입력 추가 해주면 된다.
	
	예를 들어 특정 폴더에 있는 python3로 개발된 프로그램인 mini_cts5_py3.py를 실행하는 방법은 다음과 같다.
	
	1-1 (터미널도 같이 띄우며 실행 하는 방법)
	lxterminal -e python3 /home/pi/minirobot/Python3/CTS/mini_cts5_py3.py
	
	1-2(터미널 없이 프로그램 창 띄우며 실행 하는 방법)
	python3 /home/pi/minirobot/Python3/CTS/mini_cts5_py3.py

	1-3(bash 파일을 이용한 프로그램 실행 방법, 특정 폴더에 있는 bash 작성후 삽입)
	@/home/pi/minirobot/mini_start.sh

	저장하고 재부팅 하면 mini_cts5_py3.py가 프로그램을 실행 한다.
	

2. 윈도우 창이 없는 프로그램 부팅시 자동 실행 하는 방법 ( 터미널 부팅 모드에서 가능)
	
	별도의 bash 파일을 만들고 아래 폴더에 넣어 둔다.
	/etc/profile.d