package com.perf;
import java.nio.charset.Charset;

import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Level;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.Param;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.Warmup;

import com.google.common.hash.Hasher;
import com.google.common.hash.Hashing;

public class BenchMark {

    @State(Scope.Benchmark)
    public static class ExecutionPlan {

//        @Param({ "100", "200", "300", "500", "1000" })
        @Param({ "10"})
        public int n;

//        public Hasher murmur3;
//
//        public String password = "4v3rys3kur3p455w0rd";
//
//        @Setup(Level.Invocation)
//        public void setUp() {
//            murmur3 = Hashing.murmur3_128().newHasher();
//        }
    }

//    @Fork(value = 1, warmups = 1)
//    @Benchmark
//    @BenchmarkMode(Mode.Throughput)
//    @Warmup(iterations = 5)
//    public void benchMurmur3_128(ExecutionPlan plan) {
//
//        for (int i = plan.iterations; i > 0; i--) {
//            plan.murmur3.putString(plan.password, Charset.defaultCharset());
//        }
//
//        plan.murmur3.hash();
//    }
//
    @Benchmark
    @Fork(value = 1, warmups = 1)
    @BenchmarkMode(Mode.SampleTime)
    public void init(ExecutionPlan plan) {
        fibimpl(plan.n);
    }

	
	
	public long fibimpl(int n) {
		if(n==0) return 0;
		if(n==1) return 1;
		long n1=0, n2=1, n3=1;
		for(int i=2;i<n;++i) {
			n3=n1+n2;
			n1=n2;
			n2=n3;
		}
		return n3;
	}
}