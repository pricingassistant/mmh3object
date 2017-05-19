from libc.stdint cimport uint32_t

cdef extern from "MurmurHash3.h":
	extern void MurmurHash3_x86_32(const void* key, int len, uint32_t seed, void* out)