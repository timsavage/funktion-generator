;=======================================================================
; TWI Constants
;=======================================================================
.equ TW_STATUS_MASK, 0xF8	; Status mask for TWI

.equ TW_BUS_ERROR, 0x00		; Illegal start or stop condition
.equ TW_SR_DATA_ACK, 0x80	; Data received, ACK returned

.equ TW_ST_SLA_ACK, 0xA8	; SLA+R received, ACK returned
.equ TW_ST_DATA_ACK, 0xB8	; Data transmitted, ACK received
