#!/usr/bin/env python3

import copy
import unittest

from knowledge_audit import (
    load_json,
    official_sdk_resource_map_gaps,
    production_resource_matrix_gaps,
)


class ProductionResourceMatrixAuditTest(unittest.TestCase):
    def setUp(self):
        self.matrix = load_json(
            "references/production-resource-verification-matrix.json"
        )

    def test_current_matrix_has_no_structural_gaps(self):
        self.assertEqual([], production_resource_matrix_gaps(self.matrix))

    def test_remote_material_service_cannot_be_marked_embedded(self):
        matrix = copy.deepcopy(self.matrix)
        matrix["policy"]["remote_material_service"] = "embedded"

        gaps = production_resource_matrix_gaps(matrix)

        self.assertTrue(
            any("local-only material boundary" in gap.get("reason", "") for gap in gaps)
        )

    def test_missing_external_family_is_rejected(self):
        matrix = copy.deepcopy(self.matrix)
        matrix["external_catalog"]["families"].remove("font")

        gaps = production_resource_matrix_gaps(matrix)

        self.assertTrue(
            any("required external material families" in gap.get("reason", "") for gap in gaps)
        )


class OfficialSdkResourceMapAuditTest(unittest.TestCase):
    def setUp(self):
        self.resource_map = load_json(
            "references/official-sdk-download-resource-map.json"
        )
        registry = load_json("references/sdk-module-registry.json")
        self.module_ids = {module["id"] for module in registry["modules"]}

    def test_current_map_has_no_structural_gaps(self):
        self.assertEqual(
            [],
            official_sdk_resource_map_gaps(self.resource_map, self.module_ids),
        )

    def test_absolute_package_path_is_rejected(self):
        resource_map = copy.deepcopy(self.resource_map)
        resource_map["resource_groups"][0]["relative_files"][0] = (
            r"D:\Downloads\NvAndroidStreamingSdk.jar"
        )

        gaps = official_sdk_resource_map_gaps(resource_map, self.module_ids)

        self.assertTrue(
            any(gap.get("kind") == "official_sdk_resource_paths" for gap in gaps)
        )

    def test_unknown_module_reference_is_rejected(self):
        resource_map = copy.deepcopy(self.resource_map)
        resource_map["asset_families"][0]["module_ids"].append("missing-module")

        gaps = official_sdk_resource_map_gaps(resource_map, self.module_ids)

        self.assertTrue(
            any(gap.get("kind") == "official_sdk_resource_modules" for gap in gaps)
        )


if __name__ == "__main__":
    unittest.main()
