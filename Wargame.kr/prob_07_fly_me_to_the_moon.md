# Wargame.kr No.07 - fly me to the moon

## 문제 출제 의도
난독화된 javascript 코트를 해석할 수 있는지 확인하고, 문제에서 원하는 바에 다가가기 위하여 코드를 조작하는 법을 아는지 확인한다.

## 문제 이해
문제에 접근하기 전에 `javascript game.  can you clear with bypass prevent cheating system?`가 힌트로 주어진다. 말 그대로 자바스크립트 게임이며 치팅 방지 시스템을 우회하여 게임을 클리어 할 수 있느냐? 라는 의미의 힌트이다.

문제에 접근하여 게임을 진행하면 트랙이 점점 줄어들며 이동하고 비행기가 트랙을 따라 진행하며 트랙에 부딪히지 않으며 점수에 도달하는 게임이다.

벽에 부딪히게 되면 YOU NEED `GET THE SCORE 31337.`가 출력된다.

개발자 도구를 통하여 코드 중 script태그 안의 javascript 코드를 보면 난독화 되어있음을 알 수 있다.

## 문제 해결 방안
난독화 된 자바스크립트를 해석해주는 웹사이트에 해당 소스를 스크랩하여 해석하여 보면

```javascript
var _0x32bb = ["\x6B\x69\x6C\x6C\x50\x6C\x61\x79\x65\x72", "\x63\x68\x65\x63\x6B\x4C\x69\x66\x65", "\x67\x65\x74\x53\x63\x6F\x72\x65", "\x42\x69\x6E\x63\x53\x63\x6F\x72\x65", "\x73\x68\x72\x69\x6E\x6B\x54\x75\x6E\x6E\x65\x6C", "\x77\x69\x64\x74\x68\x54\x75\x6E\x6E\x65\x6C", "\x6F\x62\x6A\x65\x63\x74", "\x44\x6F\x20\x63\x68\x65\x61\x74\x69\x6E\x67\x2C\x20\x69\x66\x20\x79\x6F\x75\x20\x63\x61\x6E", "\x77\x61\x72\x6E", "\x6F\x66\x66\x73\x65\x74\x4C\x65\x66\x74", "\x74\x75\x6E\x6E\x65\x6C", "\x67\x65\x74\x45\x6C\x65\x6D\x65\x6E\x74\x42\x79\x49\x64", "\x74\x6F\x70", "", "\x70\x78", "\x63\x73\x73", "\x64\x69\x73\x70\x6C\x61\x79", "\x62\x6C\x6F\x63\x6B", "\x65\x61\x63\x68", "\x69\x6D\x67\x2E\x6C\x65\x66\x74\x5F\x77\x61\x6C\x6C", "\x69\x6D\x67\x2E\x72\x69\x67\x68\x74\x5F\x77\x61\x6C\x6C", "\x23\x68\x69\x67\x68\x5F\x73\x63\x6F\x72\x65\x73", "\x72\x65\x6D\x6F\x76\x65", "\x74\x61\x62\x6C\x65", "\x6E\x6F\x6E\x65", "\x64\x69\x76\x23\x73\x63\x6F\x72\x65\x5F\x74\x61\x62\x6C\x65", "\x63\x6C\x69\x63\x6B", "\x74\x65\x78\x74", "\x73\x70\x61\x6E\x23\x73\x63\x6F\x72\x65", "\x6C\x65\x66\x74", "\x69\x6D\x67\x23\x73\x68\x69\x70", "\x73\x6C\x6F\x77", "\x66\x61\x64\x65\x49\x6E", "\x62\x61\x63\x6B\x67\x72\x6F\x75\x6E\x64\x2D\x70\x6F\x73\x69\x74\x69\x6F\x6E", "\x35\x30\x25\x20", "\x64\x69\x76\x23\x74\x75\x6E\x6E\x65\x6C", "\x72\x61\x6E\x64\x6F\x6D", "\x66\x6C\x6F\x6F\x72", "\x75\x70\x64\x61\x74\x65\x54\x75\x6E\x6E\x65\x6C\x28\x29", "\x66\x61\x64\x65\x4F\x75\x74", "\x50\x4F\x53\x54", "\x68\x69\x67\x68\x2D\x73\x63\x6F\x72\x65\x73\x2E\x70\x68\x70", "\x74\x6F\x6B\x65\x6E\x3D", "\x26\x73\x63\x6F\x72\x65\x3D", "\x61\x6A\x61\x78", "\x68\x74\x6D\x6C", "\x70\x23\x77\x65\x6C\x63\x6F\x6D\x65", "\x75\x70\x64\x61\x74\x65\x54\x6F\x6B\x65\x6E\x28\x29", "\x74\x68\x78\x2C\x20\x43\x68\x72\x69\x73\x74\x69\x61\x6E\x20\x4D\x6F\x6E\x74\x6F\x79\x61", "\x6D\x6F\x75\x73\x65\x6F\x76\x65\x72", "\x23\x63\x68\x72\x69\x73\x74\x69\x61\x6E", "\x6D\x6F\x75\x73\x65\x6F\x75\x74", "\x72\x65\x61\x64\x79", "\x43\x68\x72\x69\x73\x74\x69\x61\x6E\x20\x4D\x6F\x6E\x74\x6F\x79\x61", "\x70\x61\x67\x65\x58", "\x6D\x6F\x75\x73\x65\x6D\x6F\x76\x65", "\x74\x6F\x6B\x65\x6E\x2E\x70\x68\x70", "\x67\x65\x74"];
function secureGame() {
	var _0x8618x2 = this;
	var _0x8618x3 = true;
	function _0x8618x4() {
		_0x8618x3 = false;
		return true
	};
	function _0x8618x5() {
		return _0x8618x3
	};
	this[_0x32bb[0]] = function () {
		_0x8618x4();
		return true
	};
	this[_0x32bb[1]] = function () {
		return _0x8618x5()
	};
	var _0x8618x6 = 0;
	function _0x8618x7() {
		return _0x8618x6
	};
	function _0x8618x8() {
		if (_0x8618x3) {
			_0x8618x6++
		};
		return true
	};
	this[_0x32bb[2]] = function () {
		return _0x8618x7()
	};
	this[_0x32bb[3]] = function () {
		_0x8618x8();
		return true
	};
	var _0x8618x9 = 320;
	function _0x8618xa() {
		_0x8618x9 -= 20;
		return true
	};
	function _0x8618xb() {
		return _0x8618x9
	};
	this[_0x32bb[4]] = function () {
		_0x8618xa();
		return true
	};
	this[_0x32bb[5]] = function () {
		return _0x8618xb()
	}
};
var bg_val = 0;
var rail_left = 0;
var rail_right = 500;
var ship_x = 234;
var pos_x = 234;
var c_s = 0;
var c_r = 0;
var c_w = 0;
var t_state = 0;
left_wall = new Array(20);
right_wall = new Array(20);
function initTunnel() {
	BTunnelGame = new secureGame();
	if (_0x32bb[6] == typeof console) {
		console[_0x32bb[8]](_0x32bb[7])
	};
	rail_left = document[_0x32bb[11]](_0x32bb[10])[_0x32bb[9]];
	rail_right += rail_left;
	y = 0;
	for (y = 0; y < 20; y++) {
		left_wall[y] = 80;
		right_wall[y] = 400
	};
	$(_0x32bb[19])[_0x32bb[18]](function (_0x8618x16) {
		y = _0x8618x16 * 25;
		$(this)[_0x32bb[15]](_0x32bb[12], _0x32bb[13] + y + _0x32bb[14]);
		$(this)[_0x32bb[15]](_0x32bb[16], _0x32bb[17])
	});
	$(_0x32bb[20])[_0x32bb[18]](function (_0x8618x16) {
		y = _0x8618x16 * 25;
		$(this)[_0x32bb[15]](_0x32bb[12], _0x32bb[13] + y + _0x32bb[14]);
		$(this)[_0x32bb[15]](_0x32bb[16], _0x32bb[17])
	});
	$(_0x32bb[25])[_0x32bb[26]](function () {
		$(_0x32bb[23])[_0x32bb[22]](_0x32bb[21]);
		$(_0x32bb[25])[_0x32bb[15]](_0x32bb[16], _0x32bb[24]);
		restartTunnel();
		updateTunnel()
	})
};
function restartTunnel() {
	BTunnelGame = new secureGame();
	if (_0x32bb[6] == typeof console) {
		console[_0x32bb[8]](_0x32bb[7])
	};
	ship_x = 234;
	c_s = 0;
	c_r = 0;
	c_w = 0;
	$(_0x32bb[28])[_0x32bb[27]](_0x32bb[13] + 0);
	$(_0x32bb[30])[_0x32bb[15]](_0x32bb[29], ship_x + _0x32bb[14]);
	y = 0;
	for (y = 0; y < 20; y++) {
		left_wall[y] = 80;
		right_wall[y] = 400
	};
	$(_0x32bb[30])[_0x32bb[32]](_0x32bb[31]);
	$(_0x32bb[19])[_0x32bb[18]](function (_0x8618x16) {
		y = _0x8618x16 * 25;
		$(this)[_0x32bb[15]](_0x32bb[12], _0x32bb[13] + y + _0x32bb[14]);
		$(this)[_0x32bb[15]](_0x32bb[16], _0x32bb[17])
	});
	$(_0x32bb[20])[_0x32bb[18]](function (_0x8618x16) {
		y = _0x8618x16 * 25;
		$(this)[_0x32bb[15]](_0x32bb[12], _0x32bb[13] + y + _0x32bb[14]);
		$(this)[_0x32bb[15]](_0x32bb[16], _0x32bb[17])
	})
};
function updateTunnel() {
	bg_val = bg_val + 2;
	if (bg_val > 20) {
		bg_val = 0
	};
	$(_0x32bb[35])[_0x32bb[15]](_0x32bb[33], _0x32bb[34] + bg_val + _0x32bb[14]);
	if (ship_x + 32 < 500) {
		if (ship_x + 46 < pos_x) {
			ship_x += 4
		} else {
			if (ship_x + 16 < pos_x) {
				ship_x += 2
			}
		}
	};
	if (ship_x > 0) {
		if (ship_x - 14 > pos_x) {
			ship_x -= 4
		} else {
			if (ship_x + 16 > pos_x) {
				ship_x -= 2
			}
		}
	};
	$(_0x32bb[30])[_0x32bb[15]](_0x32bb[29], ship_x + _0x32bb[14]);
	c_r++;
	if (c_r > 60) {
		c_r = 0;
		t_state = Math[_0x32bb[37]](Math[_0x32bb[36]]() * 2)
	};
	if (left_wall[0] < 10) {
		t_state = 1
	} else {
		if (right_wall[0] > 470) {
			t_state = 0
		}
	};
	y = 0;
	for (y = 20; y > 0; y--) {
		left_wall[y] = left_wall[y - 1];
		right_wall[y] = right_wall[y - 1]
	};
	if (t_state == 0) {
		left_wall[0] -= 3
	};
	if (t_state == 1) {
		left_wall[0] += 3
	};
	right_wall[0] = left_wall[0] + BTunnelGame[_0x32bb[5]]();
	$(_0x32bb[19])[_0x32bb[18]](function (_0x8618x16) {
		$(this)[_0x32bb[15]](_0x32bb[29], _0x32bb[13] + left_wall[_0x8618x16] + _0x32bb[14])
	});
	$(_0x32bb[20])[_0x32bb[18]](function (_0x8618x16) {
		$(this)[_0x32bb[15]](_0x32bb[29], _0x32bb[13] + right_wall[_0x8618x16] + _0x32bb[14])
	});
	if (BTunnelGame[_0x32bb[5]]() >= 120) {
		c_w++;
		if (c_w > 100) {
			c_w = 0;
			BTunnelGame[_0x32bb[4]]();
			left_wall[0] += 10
		}
	};
	c_s++;
	if (c_s > 20) {
		c_s = 0;
		BTunnelGame.BincScore();
		$(_0x32bb[28])[_0x32bb[27]](_0x32bb[13] + BTunnelGame[_0x32bb[2]]())
	};
	if (ship_x <= left_wall[18] + 20 || ship_x + 32 >= right_wall[18]) {
		BTunnelGame[_0x32bb[0]]()
	};
	if (BTunnelGame[_0x32bb[1]]()) {
		setTimeout(_0x32bb[38], 10)
	} else {
		$(_0x32bb[30])[_0x32bb[39]](_0x32bb[31]);
		$(_0x32bb[19])[_0x32bb[15]](_0x32bb[16], _0x32bb[24]);
		$(_0x32bb[20])[_0x32bb[15]](_0x32bb[16], _0x32bb[24]);
		$[_0x32bb[44]]({
			type: _0x32bb[40],
			url: _0x32bb[41],
			data: _0x32bb[42] + token + _0x32bb[43] + BTunnelGame[_0x32bb[2]](),
			success: function (_0x8618x19) {
				showHighScores(_0x8618x19)
			}
		})
	}
};
function scoreUpdate() {
	return
};
function showHighScores(_0x8618x19) {
	$(_0x32bb[25])[_0x32bb[45]](_0x8618x19);
	$(_0x32bb[25])[_0x32bb[15]](_0x32bb[16], _0x32bb[17])
};
$(document)[_0x32bb[52]](function () {
	$(_0x32bb[46])[_0x32bb[15]](_0x32bb[16], _0x32bb[17]);
	updateToken();
	setInterval(_0x32bb[47], 10000);
	$(_0x32bb[46])[_0x32bb[26]](function () {
		$(_0x32bb[46])[_0x32bb[15]](_0x32bb[16], _0x32bb[24]);
		initTunnel();
		updateTunnel()
	});
	$(_0x32bb[50])[_0x32bb[49]](function () {
		$(this)[_0x32bb[45]](_0x32bb[48])
	});
	$(_0x32bb[50])[_0x32bb[51]](function () {
		$(this)[_0x32bb[45]](temp)
	})
});
var temp = _0x32bb[53];
$(document)[_0x32bb[55]](function (_0x8618x1d) {
	pos_x = _0x8618x1d[_0x32bb[54]] - rail_left
});
var token = _0x32bb[13];
function updateToken() {
	$[_0x32bb[57]](_0x32bb[56], function (_0x8618x20) {
		token = _0x8618x20
	})
};
```
위와 같은 코드가 출력되는데 첫 _0x32bb 변수는 배열을 담고 있었다.

그리고
```javascript
$[_0x32bb[44]]({
			type: _0x32bb[40],
			url: _0x32bb[41],
			data: _0x32bb[42] + token + _0x32bb[43] + BTunnelGame[_0x32bb[2]](),
			success: function (_0x8618x19) {
				showHighScores(_0x8618x19)
			}
        })
```
이 부분을 보면 type과 url, data, success 가 있는것을 보아 통신이 이루어지는 부분임을 추측할 수 있어 _0x32bb 배열의 값을 찾아보기 위하여 python을 이용하였다. 

_0x32bb[40]의 경우 `'POST'`이고 _0x32bb[41]의 경우는 `'high-scores.php'`, 0x32bb[42]는 `'token='`, _0x32bb[43]은 `'&score='`임을 알 수 있었다.

이 부분을 보아 이 코드를 조금 수정해준다면 치팅 방지 시스템을 우회할 수 있을 것으로 보이는데 score를 항상 통과기준인 31337이면 될것 같아서 위의 코드를

```javascript
$ajax({
    type:'POST',
    url:'high-scores.php',
    data: 0x32bb[42] + token + _0x32bb[43] + '31337',
    success: function (_0x8618x19) {
        showHighScores(_0x8618x19)
    }
})
```
로 수정하여 코드를 개발자 도구의 콘솔창에 입력하여줬고 게임을 시작하여 벽에 부딪히자 flag를 출력해주었다.

해당 flag를 auth에 입력해주면 문제풀이에 성공한다.