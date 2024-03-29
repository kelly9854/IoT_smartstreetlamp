# IoT_smartstreetlamp
스마트 가로등 구현(arduino, rasberrypi 이용)

개발주제
(과 제 명)

스마트 가로등


개발도구

라즈베리 파이, 아두이노


개발배경

저희 팀은 일상생활에서 많이 볼 수 있는 가로등을 이용하기로 하였습니다. 
우선 가로등은 현재 우리나라에 270만 개가 배치되어있어 이미 구축된 인프라를 가지고 있습니다. 
그래서 배치된 환경에서 다른 기능들을 추가하여 활용할 수 있어서 활용가치가 높습니다. 
그래서 이 가로등을 조형물이나 빛을 밝히는 도구뿐만 아니라 다른 가치를 창출할 수 없을까 하는 고민에서 다음과 같은 시제품을 개발하게 되었습니다.


개발내용

처음에 저희 팀은 사회안전을 목표로 범죄자 검거 및 범죄 예방을 위해 일상생활에서 많이 볼 수 있는 가로등을 이용하기로 하였습니다. 
하지만 개발과정에서 머신러닝 부분에서 문제가 있었고 우선 범죄자를 검거하기 위해서 범죄자에 대한 얼굴이나 모션의 데이터가 필요한데 
이를 수집하기에 한국에서는 개인 정보의 문제로 실현이 어려울 것 같았습니다. 
그래서 주어진 환경에서 다른 문제를 해결할 수 없을까 하는 고민을 하게 되었고 팀과 함께 개발주제를 수정하고 구체화하기 위해 여러 회의를 거쳤습니다. 
그 결과 저희는 전국의 모든 가로등을 각각 하나의 작은 데이터마이닝센터로 바꾸는 것을 목표로 다양한 문제를 해결할 수 있도록 하고 
치매 노인이나 유아 등 노약자의 실종 상황 시 빠른 발견에 도움을 주는 것에 중점을 두고 개발하였습니다. 
서비스를 이용하기 위해 실종의 우려가 있는 사람들의 이미지를 미리 받거나 실종 후 받습니다. 
이 경우에서는 사람들이 오히려 데이터를 주고 원하는 상황이므로 데이터 수집에 대한 문제점을 해결할 수 있습니다. 
수집된 데이터를 이용해 머신러닝의 이미지 프로세싱 기술로 가로등의 카메라와 모션 센서를 통해 
대상의 이미지 및 이동 반경을 분석하여 실종 시 빠른 발견에 도움을 줄 수 있습니다. 
저희가 현재까지 진행한 상황은 아두이노의 센서들을 통해서 정보를 받고 데이터를 가져올 수 있으며 
이미지 센싱을 위해서 라즈베리 파이의 카메라를 사용하기 때문에 아두이노와 라즈베리 파이를 통신하고 있습니다. 
그리고 라즈베리 파이에서 머신러닝을 구현하고 있는데 아직 정확성이 떨어져 많은 데이터를 수집하고 여러 방법을 시도하는 중입니다. 
추가로 저희 스마트 가로등은 카메라와 모션센서뿐만 아니라 온습도 센서, 유해 가스 센서 등의 다양한 센서들을 탑재합니다. 
이 센서들을 통해 가로등은 다양한 데이터를 수집하고 데이터를 이용하여 다양한 서비스들을 가능하게 합니다. 


결과물
형태

실종 문제를 해결하는 것을 중점으로 두고 시제품을 개발하였기 때문에 이 결과물에 관해 설명하자면 
치매 노인이나 유아 등 노약자, 반려동물의 실종 시에 사진을 라즈베리 파이에 데이터들을 줘서 학습하게 하고 
라즈베리 파이와 아두이노는 통신합니다. 카메라를 통해서 라즈베리 파이에서 이미지를 인식합니다. 
미아와 치매 노인의 경우는 영상을 통해서 키와 이미지, 걸음걸이 등으로 분석하고 정확성이 어느 정도 이상일 때 사진을 보내서 확인합니다. 
모션 센서를 통해서는 찾고자 하는 대상의 이동 반경을 조사할 수 있습니다. 또한 시제품으로는 정확한 인식은 부족하지만 반려동물에도 적용 가능합니다.
더 나아가 센서들을 통해서 얻은 데이터로 주차 공간에 대한 정보 제공, 금연 구역에서의 흡연 여부, 현재 미세먼지 농도와 온습도를 
LCD에 안내하는 서비스, 농촌이나 독거노인이 생활하는 곳에서 일정 기간 이상 집에서 출입이 없을 때 담당 기관에서 대상 집을 방문해 
고독사를 예방하는 서비스가 가능합니다. 또한, 교통정보 및 유해 가스, 기상 데이터를 수집하여 빅데이터를 구축할 수 있습니다. 
스마트시티를 위한 스마트 가로등은 사람들에게 빠른 변화를 만들어줄 것입니다. 이미 구축된 인프라를 사용하므로 개발에 있어서 
보다 적은 시간 안에 구현할 수 있으며 전국의 모든 가로등을 각각 하나의 작은 데이터마이닝센터로 바꾸는 것은 활용가치가 상당히 높습니다. 

