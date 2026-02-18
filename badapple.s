.globl _start
.data
	length: .word 4096
	videofile: .asciz "bad_apple.dat"
	audiofile: .asciz "bad_apple_audio.dat"
.text
_start:
	la t2, length
	addi t4, t2, 50
	lw t2, 0(t2)
	add s8, t4, t2
	add s9, t4, zero
	addi s1, zero, 0xFF
	add s0, zero, zero
	addi s3, zero, 32
	slli s3, s3, 2
	add t5, zero, zero
	add s2, zero, zero
	addi s4, zero, 1
	addi s5, s1, 1
	li t0, 0x10040000
	#add s2, s2, zero 
	li t1, 0x00FFFFFF
	#add t1, zero, zero
	la a0, videofile
	jal OPENFILE
	add s7, zero, a0
	addi s11, zero, 1
	jal READFILE
CALLLOOP:
	addi t3, zero, 186
	#bge t5, t2, exit
	remu t6, t5, t3
	ble t4, s8, SKIPFILEREAD
	jal READFILE 
SKIPFILEREAD:
	bgt t6, zero, NORESET
	#blt t5, t3, NORESET
	beq t6, s4, NORESET
	#jal READFILE 
	li t0, 0x10040000
   	#add t5, zero, zero
	#add s2, s2, zero 
	add t1, zero, zero
NORESET:
	lbu  t3, 0(t4)
	blt s0, s1, COLORCHOICE
ENDCOLORCHOICE:
	add s0, s0, t3
	jal DRAW	
	addi t4, t4, 1
	add s4, t6, zero
	j CALLLOOP
exit:
	addi x17, zero, 10
	ecall
	
DRAW:
	beq t3, s11 DRAWSINGLEPIXEL
	blez t3, ENDDRAW
	addi t3, t3, -2
	sd t1, 0(t0)
	addi t0, t0, 8
	j DRAW
DRAWSINGLEPIXEL:
	sw t1, 0(t0)
	addi t0, t0, 4
ENDDRAW:
	blt s0, s1, RETURNDRAW
	sub s0, s0, s5
	slli s0, s0, 2
	sub t0, t0, s0
	addi t5, t5, 1
	li t1, 0
	add s0, zero, zero
RETURNDRAW:
	jalr zero, ra, 0
	
COLORCHOICE:
	not t1, t1
	j ENDCOLORCHOICE
OPENFILE:
	addi x17, zero, 1024 
	add a1, zero, zero
	ecall
	jalr zero, 0(ra)
READFILE:
	addi x17, zero, 63 
	add a0, zero, s7
	add t4, zero, s9
	add a1, zero, s9
	add a2, zero, t2
	ecall
	jalr zero, 0(ra)

