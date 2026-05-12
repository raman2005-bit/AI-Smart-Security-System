import cv2,time
from ultralytics import YOLO
from cinfig_manager import call_sms,check_if_open,set_system_status
from bot_hendler import send_telegram_msg,send_telegram_photo,check_telegram_for_reset

model = YOLO('yolov8n.pt')
lt = 0
lsc = 0
last_tele_check = 0
tele_check_interval = 5
alt_cooldown = 60
status_file = "status.txt"  

cap = cv2.VideoCapture(0)
print("Security System Started")
while True:
    current_t = time.time()
    ret, frame = cap.read()
    if not ret:
        break

    is_open = check_if_open(status_file)
    if not is_open:
        cv2.putText(frame, "SYSTEM LOCKED: Send 'ok to reset", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255), 2)
        if current_t - last_tele_check > tele_check_interval:
            check_telegram_for_reset()
            last_tele_check = current_t

    else:
        result = model(frame, stream=True, conf=0.5)
        person_detected = False
        for r in result:
            for box in r.boxes:
                if int(box.cls[0]) == 0:
                    person_detected = True
                    break
    
        if person_detected and (current_t - lt > alt_cooldown) and check_if_open(status_file):
                print("seanding aleart.....")
                cv2.imwrite("alert.jpg", frame)
                send_telegram_msg("Security Alert: Movement Detected!")
                call_sms("alert.jpg")
                send_telegram_photo("alert.jpg")
                set_system_status("locked")
                lt = current_t
                print("System locked send 'ok' on Telegram to reset")
                
    cv2.imshow("security feed",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()