from vector import Vector


class VectorTests:

    @staticmethod
    def test_magnitude():
        v1 = Vector([-0.221, 7.437])
        v2 = Vector([8.813, -1.331, -6.247])

        v3 = Vector([5.581, -2.136])
        v4 = Vector([1.996, 3.108, -4.554])

        print(f"|v1| = {v1.magnitude()} |v2| {v2.magnitude()} n v3= {v3.normalize()} n v4= {v4.normalize()}")

    @staticmethod
    def test_angles():
        v1 = Vector([7.887, 4.138])
        v2 = Vector([-8.802, 6.776])

        v3 = Vector([-5.995, -4.904, -1.874])
        v4 = Vector([-4.496, -8.755, 7.103])

        v5 = Vector([3.183, -7.627])
        v6 = Vector([-2.668, 5.319])

        v7 = Vector([7.35, 0.221, 5.188])
        v8 = Vector([2.751, 8.259, 3.985])

        print(f"v1v2 = {v1.dot_product(v2)}")
        print(f"v3v4 = {v3.dot_product(v4)}")
        print(f"angle rad v5v6 = {v5.angle(v6)}")
        print(f"angle degree v7v8 = {v7.angle(v8, True)}")

    @staticmethod
    def test_parallel_orthogonal():
        v1 = Vector([-7.579, -7.88])
        v2 = Vector([22.737, 23.64])

        v3 = Vector([-2.029, 9.97, 4.172])
        v4 = Vector([-9.231, -6.639, -7.245])

        v5 = Vector([-2.328, -7.284, -1.214])
        v6 = Vector([-1.821, 1.072, -2.94])

        v7 = Vector([2.118, 4.827])
        v8 = Vector([0, 0])

        print(f"p:{v1.is_parallel(v2)} o:{v1.is_orthogonal(v2)}")
        print(f"p:{v3.is_parallel(v4)} o:{v3.is_orthogonal(v4)}")
        print(f"p:{v5.is_parallel(v6)} o:{v5.is_orthogonal(v6)}")
        print(f"p:{v7.is_parallel(v8)} o:{v7.is_orthogonal(v8)}")

    @staticmethod
    def test__projection():
        v1 = Vector([3.039, 1.879])
        v2 = Vector([0.825, 2.036])

        v3 = Vector([-9.88, -3.264, -8.159])
        v4 = Vector([-2.155, -9.353, -9.473])

        v5 = Vector([3.009, -6.172, 3.692, -2.51])
        v6 = Vector([6.404, -9.144, 2.759, 8.718])

        print(f"projection:{v1.proj(v2)}")

        proj_v3 = v3.proj(v4)
        ort_v3 = v3.__sub__(proj_v3)

        print(f"v_ort:{ort_v3}")

        proj_v5 = v5.proj(v6)
        ort_v5 = v5 - proj_v5;

        print(f"v5 = {proj_v5} + {ort_v5}")

    @staticmethod
    def test__cross_product():
        v = Vector([8.462, 7.893, -8.187])
        w = Vector([6.984, -5.975, 4.778])

        cross = v.cross_product(w)

        print(f"vxw = {cross}")

        v = Vector([-8.987, -9.838, 5.031])
        w = Vector([-4.268, -1.861, -8.866])

        parallelogram = v.parallelogram_area(w)

        print(f"parallelogram = {parallelogram}")

        v = Vector([1.5, 9.547, 3.691])
        w = Vector([-6.007, 0.124, 5.772])

        triangle = v.triangle_area(w)

        print(f"triangle = {triangle}")