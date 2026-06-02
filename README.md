# iPodSync

> 2020년대의 영상 콘텐츠를 2000년대 iPod에서 가장 쉽게 재생할 수 있게 하는 프로그램

---

# 탄생 배경

iPod Classic은 현재도 뛰어난 음악 감상 기기이지만, 현대의 영상 포맷(WebM, MKV, H.265 등)을 직접 재생할 수 없다.  
특히 iPod Video(5세대)는 다음과 같은 제약이 존재한다.

- H.264 Baseline Profile 필요
- AAC 오디오 필요
- 제한된 해상도 지원
- 최신 YouTube 포맷 미지원
- iTunes를 통한 동기화 필요

현재 사용자는 다음 과정을 직접 수행해야 한다.

1. YouTube 링크 복사
2. yt-dlp로 다운로드
3. FFmpeg 명령어 입력
4. iPod 호환 포맷으로 변환
5. iTunes로 전송
6. iPod 동기화

Handbrake같은 프로그램이 있으나, 복잡스럽고 무겁다. 반면에 iPodSync의 목적은 이 과정을 최대한 자동화하는 것이다.

---

# 프로젝트 목표

# 단기 목표
iPod Classic Gen5에서 재생 가능한 영상을 자동 생성한다.  
사용자는 원하는 유튜브 링크 입력만 수행하고, 변환 등의 나머지 업무는 프로그램이 처리한다.

## 중기 목표
여러 세대 iPod을 지원한다.

| 세대 | 모델 |
|------|------|
| Gen4 | iPod Photo |
| Gen5 | iPod Video |
| Gen6 | iPod Classic |
| Gen7 | iPod Classic |

### 장기 목표
실행 파일로 배포한다.

| 플랫폼 | 배포 형태 |
|--------|-----------|
| macOS  | `iPodSync.app` |
| Windows | `iPodSync.exe` |

---

## 개발 로드맵

### v0.1 — 최초 공개 버전

상태: 완료

- yt-dlp 연동
- FFmpeg 연동
- Gen5 호환 M4V 생성
- GitHub 저장소 생성

---

### v0.2 — 다운로드 자동화 개선

상태: 개발 중  
목표: 실사용 가능한 CLI 구축

- 다중 URL 입력
- 다운로드 대기열 표시
- `archivev` 자동 이동
- 중복 변환 방지
- 변환 통계 출력

---

### v0.3 — 메뉴형 CLI

기존 프롬프트 방식에서 메뉴 시스템으로 개선한다.

1. Download Video
2. Download Playlist
3. Convert Existing Files
4. Settings
5. Exit

- 설정 저장
- 기존 영상 재변환
- 장치 선택
- 고·중·저화질 선택

---

### v0.4 — 장치 프로파일 시스템

프로그램 시작 시 장치를 선택하면 FFmpeg 프리셋이 자동 적용된다.

Q: Which iPod are you using?

1. Gen4
2. Gen5
3. Gen6
4. Gen7

---

### v0.5 — 재생목록 지원

- YouTube Playlist 자동 다운로드
- 재생목록 폴더 생성
- 이어받기
- 중복 제거

---

### v1.0 — 정식 공개판

목표: 실제 사용 가능한 안정적인 프로젝트

- 안정화
- README 정비
- 설정 파일
- 로그 시스템
- 에러 리포트
- GitHub Release

---

### v1.5 — iTunes 연동 보조 기능

변환 후 iTunes 작업을 최소화한다.

- VMware 공유폴더 지원
- 자동 복사
- Import 폴더 생성

---

### v2.0 — GUI 버전

기술: PySide6  
목표: 터미널 사용 그만


+----------------------------------+
|           iPodSync               |
+----------------------------------+
  YouTube URL
  [________________________]
  [        Download        ]

  Device: Gen5
  Output: changedv
+----------------------------------+

---

### v2.5 — 드래그 앤 드롭

영상 파일을 창에 끌어놓으면 자동으로 변환된다.

---

### v3.0 — 배포 버전

사용자는 Python 설치 없이 바로 실행할 수 있다.

| 플랫폼 | 파일 |
|--------|------|
| macOS  | `iPodSync.app` |
| Windows | `iPodSync.exe` |

---

### v4.0 — 멀티 디바이스 지원

- iPod Photo
- iPod Video
- iPod Classic
- iPod Nano
- Video Podcast

---

## 최종 비전
언젠가는 만들 수 있겠지?

# iPodSync

> The easiest way to watch modern video content on a classic iPod.

---

# Background

The iPod Classic is still a great media player, but it cannot natively play modern video formats like WebM, MKV, or H.265.  
The **iPod Video (5th gen)** in particular has strict requirements:

- H.264 Baseline Profile required
- AAC audio required
- Limited resolution support
- No support for modern YouTube formats
- Sync only via iTunes

Currently, users have to do all of this manually:

1. Copy the YouTube link
2. Download with yt-dlp
3. Run FFmpeg manually
4. Convert to an iPod-compatible format
5. Transfer to iTunes
6. Sync to iPod

Tools like HandBrake exist, but they're complex and heavy. iPodSync is built to automate this entire process as simply as possible.

---

# Goals

## Short-term
Automatically generate iPod Gen5-compatible video files.  
The user only inputs a YouTube link — the rest is handled by the program.

## Mid-term
Support multiple iPod generations.

| Generation | Model |
|------------|-------|
| Gen4 | iPod Photo |
| Gen5 | iPod Video |
| Gen6 | iPod Classic |
| Gen7 | iPod Classic |

## Long-term
Distribute as a standalone executable.

| Platform | Format |
|----------|--------|
| macOS | `iPodSync.app` |
| Windows | `iPodSync.exe` |

---

## Roadmap

### v0.1 — Initial Release

Status: Complete

- yt-dlp integration
- FFmpeg integration
- Gen5-compatible M4V output
- GitHub repository created

---

### v0.2 — Download Automation

Status: In development  
Goal: A usable CLI for everyday use

- Multiple URL input
- Download queue display
- Auto-move to `archivev`
- Duplicate conversion prevention
- Conversion statistics output

---

### v0.3 — Menu-based CLI

Replaces the current prompt-only interface with a menu system.

```
1. Download Video
2. Download Playlist
3. Convert Existing Files
4. Settings
5. Exit
```

- Settings persistence
- Re-convert existing files
- Device selection
- Quality selection (high / medium / low)

---

### v0.4 — Device Profile System

Select your iPod at startup and FFmpeg presets are applied automatically.

```
Which iPod are you using?

1. Gen4
2. Gen5
3. Gen6
4. Gen7
```

---

### v0.5 — Playlist Support

- Auto-download YouTube playlists
- Create playlist folders
- Resume interrupted downloads
- Duplicate removal

---

### v1.0 — Stable Release

Goal: A reliable, production-ready project

- Stability improvements
- Polished README
- Config file support
- Logging system
- Error reporting
- GitHub Release

---

### v1.5 — iTunes Integration Helper

Minimize manual iTunes steps after conversion.

- VMware shared folder support
- Auto file copy
- Auto-create Import folder

---

### v2.0 — GUI

Technology: PySide6  
Goal: No more terminal

```
+----------------------------------+
|           iPodSync               |
+----------------------------------+
  YouTube URL
  [________________________]
  [        Download        ]

  Device: Gen5
  Output: changedv
+----------------------------------+
```

---

### v2.5 — Drag and Drop

Drop a video file onto the window and it converts automatically.

---

### v3.0 — Distributable Build

No Python installation required.

| Platform | File |
|----------|------|
| macOS | `iPodSync.app` |
| Windows | `iPodSync.exe` |

---

### v4.0 — Multi-device Support

- iPod Photo
- iPod Video
- iPod Classic
- iPod Nano
- Video Podcast

---

## Final Vision
Maybe someday.