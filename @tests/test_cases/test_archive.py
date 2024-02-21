#!/usr/bin/env python3

#pyright: reportUnknownMemberType=false, reportMissingTypeStubs=false

import unittest
import uuid

from parameterized import parameterized

from palworld_save_tools.archive import UUID, FArchiveReader, FArchiveWriter

class TestArchive(unittest.TestCase):
    @parameterized.expand(
        [
            (1.0, 1.0, 1.0),
            (0.0, 0.0, 0.0),
            (-1.0, -1.0, -1.0),
            (0.0, 0.0, 1.0),
            (0.0, 1.0, 0.0),
            (1.0, 0.0, 0.0),
            (0.0, 0.0, -1.0),
            (0.0, -1.0, 0.0),
            (-107929.0, -1815, 682),
            (107929, 1815, 682),
            (107929, -1815, -682),
            (-107929, 1815, -682),
            (12345678.0, -12345678.0, 12345678.0),
            (-12345678.0, 12345678.0, -12345678.0),
            (12345678.0, 12345678.0, -12345678.0),
            (-12345678.0, -12345678.0, 12345678.0),
        ]
    )
    def test_packed_vector_roundtrip(self, x: float, y: float, z: float):
        writer = FArchiveWriter()
        writer.packed_vector(1, x, y, z)
        reader = FArchiveReader(writer.bytes())
        x_e, y_e, z_e = reader.packed_vector(1)
        self.assertEqual(x, x_e)
        self.assertEqual(y, y_e)
        self.assertEqual(z, z_e)

    def test_uuid_wrapper_matches_stdlib(self):
        test_uuid = "c1b41f12-90d3-491f-be71-b34e8e0deb5a"
        expected = uuid.UUID(test_uuid)
        b = expected.bytes
        ue_bytes = bytes(
            [
                b[0x3],
                b[0x2],
                b[0x1],
                b[0x0],
                b[0x7],
                b[0x6],
                b[0x5],
                b[0x4],
                b[0xB],
                b[0xA],
                b[0x9],
                b[0x8],
                b[0xF],
                b[0xE],
                b[0xD],
                b[0xC],
            ]
        )
        wrapper = UUID(ue_bytes)
        self.assertEqual(str(expected), str(wrapper))

    def test_uuid_wrapper_can_be_used_as_dict_key(self):
        test_uuid = "c1b41f12-90d3-491f-be71-b34e8e0deb5a"
        wrapper = UUID.from_str(test_uuid)
        d = {wrapper: "test"}
        self.assertEqual("test", d[wrapper])

    def test_uuid_wrapper_can_be_used_as_set_member(self):
        test_uuid = "c1b41f12-90d3-491f-be71-b34e8e0deb5a"
        wrapper = UUID.from_str(test_uuid)
        s = {wrapper}
        self.assertEqual(1, len(s))
        self.assertTrue(wrapper in s)

    def test_uuid_wrapper_equality(self):
        test_uuid = "c1b41f12-90d3-491f-be71-b34e8e0deb5a"
        wrapper = UUID.from_str(test_uuid)
        wrapper2 = UUID.from_str(test_uuid)
        self.assertEqual(wrapper, wrapper2)

    def test_uuid_wrapper_inequality(self):
        test_uuid = "c1b41f12-90d3-491f-be71-b34e8e0deb5a"
        wrapper = UUID.from_str(test_uuid)
        wrapper2 = UUID.from_str("c1b41f12-90d3-491f-be71-b34e8e0deb5b")
        self.assertNotEqual(wrapper, wrapper2)

    def test_uuid_wrapper_hash(self):
        test_uuid = "c1b41f12-90d3-491f-be71-b34e8e0deb5a"
        wrapper = UUID.from_str(test_uuid)
        wrapper2 = UUID.from_str(test_uuid)
        self.assertEqual(hash(wrapper), hash(wrapper2))
