import os, time
import json, math
import concurrent.futures
from urllib.parse import urlencode

from mediamatch_sdk.asset.model import MatchInfoRetrieve, ContentCategory
from mediamatch_sdk.base_client import BaseClient
from mediamatch_sdk.util.util import extract_error_message


class VideoAsset(BaseClient):
    default_retrieve_page_size = 500

    def __init__(self, access_token):
        super().__init__(access_token)  # Initialize the BaseClient with the access token

    def update_video_asset_metadata(self, asset_id, metadata):
        response = self._put(path=f"/openapi/asset/v1/video/assets/{asset_id}", json=metadata)
        if response.status_code == 200:
            return response.json()
        else:
            error_msg = extract_error_message(response)
            raise Exception(f"Failed to update the metadata of this video asset.\nError Message: {error_msg}")

    def get_video_asset_metadata(self, asset_id):
        response = self._get(path=f"/openapi/asset/v1/video/assets/{asset_id}/metadata")
        if response.status_code == 200:
            return response.json()
        else:
            error_msg = extract_error_message(response)
            raise Exception(f"Failed to get the metadata of this video asset.\nError Message: {error_msg}")

    def query_video_asset_metadata(self, page: int = None, pageSize: int = None,
                                   contentCategories: list[ContentCategory] = None,
                                   tags: list[str] = None):
        params = []
        if page is not None:
            params.append(('page', page))
        if pageSize is not None:
            params.append(('pageSize', pageSize))
        if contentCategories is not None:
            for contentCategory in contentCategories:
                params.append(('contentCategories', contentCategory.value))
        if tags is not None:
            for tag in tags:
                params.append(('tags', tag))

        query_string = urlencode(params)
        response = self._get(path=f"/openapi/asset/v1/video/assets/metadata?{query_string}")

        if response.status_code == 200:
            return response.json()
        else:
            error_msg = extract_error_message(response)
            raise Exception(f"Failed to query the metadata of video asset.\nError Message: {error_msg}")

    def __get_asset_total_count__(self, contentCategories: list[str] = None, tags: list[str] = None) -> int:
        resp = self.query_video_asset_metadata(page=1, pageSize=5, contentCategories=contentCategories, tags=tags)
        return resp.get('data', {}).get('total', 0)

    def retrieve_all_asset_metadata(self, contentCategories: list[str] = None, tags: list[str] = None):
        asset_total_count = self.__get_asset_total_count__(contentCategories, tags)
        total_page_number = math.ceil(asset_total_count / self.default_retrieve_page_size)
        print("retrieve_all_asset_metadata, total_page_number:", total_page_number)

        # key: page, value: list<metadataInfo>
        asset_metadata_dict = {}
        cur_asset_count = 0
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            futures = [executor.submit(self.query_video_asset_metadata, i + 1, self.default_retrieve_page_size,
                                       contentCategories, tags) for i in range(total_page_number)]

        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            page = result.get("data").get("page")
            meta_info_list = result.get("data").get("metadataInfoList")
            asset_metadata_dict[page] = meta_info_list
            cur_asset_count += len(meta_info_list)
        asset_metadata_list = []
        for i in range(total_page_number):
            asset_metadata_list.extend(asset_metadata_dict[i + 1])
        return asset_metadata_list

    def get_video_asset_other_info(self, asset_id):
        response = self._get(path=f"/openapi/asset/v1/video/assets/{asset_id}/information")
        if response.status_code == 200:
            return response.json()
        else:
            error_msg = extract_error_message(response)
            raise Exception(f"Failed to get other information of this video asset.\nError Message: {error_msg}")

    def query_video_asset_other_info(self, page: int = None, pageSize: int = None,
                                     contentCategories: list[ContentCategory] = None):
        params = []
        if page is not None:
            params.append(('page', page))
        if pageSize is not None:
            params.append(('pageSize', pageSize))
        if contentCategories is not None:
            for contentCategory in contentCategories:
                params.append(('contentCategories', contentCategory.value))
        query_string = urlencode(params)
        response = self._get(path=f"/openapi/asset/v1/video/assets/information?{query_string}")
        if response.status_code == 200:
            return response.json()
        else:
            error_msg = extract_error_message(response)
            raise Exception(f"Failed to query the other information of video asset.\nError Message: {error_msg}")

    def retrieve_all_asset_other_info(self, contentCategories: list[str] = None):
        asset_total_count = self.__get_asset_total_count__(contentCategories=contentCategories)
        total_page_number = math.ceil(asset_total_count / self.default_retrieve_page_size)
        print("retrieve_all_asset_other_info, total_page_number:", total_page_number)

        # key: page, value: list<otherInfo>
        asset_other_info_dict = {}
        cur_asset_count = 0
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            futures = [executor.submit(self.query_video_asset_other_info, i + 1, self.default_retrieve_page_size,
                                       contentCategories) for i in range(total_page_number)]

            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                page = result.get("data").get("page")
                other_info_list = result.get("data").get("otherInfoList")
                asset_other_info_dict[page] = other_info_list
                cur_asset_count += len(other_info_list)
        asset_other_info_list = []
        for i in range(total_page_number):
            asset_other_info_list.extend(asset_other_info_dict[i + 1])
        return asset_other_info_list

    def activate_video_asset(self, asset_id):
        response = self._post(path=f"/openapi/asset/v1/video/assets/{asset_id}/activate")
        if response.status_code == 200:
            return response.json()
        else:
            error_msg = extract_error_message(response)
            raise Exception(f"Failed to activate the video asset.\nError Message: {error_msg}")

    def deactivate_video_asset(self, asset_id):
        response = self._post(path=f"/openapi/asset/v1/video/assets/{asset_id}/deactivate")
        if response.status_code == 200:
            return response.json()
        else:
            error_msg = extract_error_message(response)
            raise Exception(f"Failed to deactivate the video asset.\nError Message: {error_msg}")

    def get_video_match(self, asset_id, start_time, end_time, page=None, pageSize=None):
        if (page == None or pageSize == None):
            response = self._get(path=f"openapi/asset/v1/video/assets/{asset_id}/matchinfo?startTime={start_time}&endTime={end_time}")
        else:
            response = self._get(path=f"openapi/asset/v1/video/assets/{asset_id}/matchinfo?startTime={start_time}&endTime={end_time}&page={page}&pageSize={pageSize}")
        if response.status_code == 200:
            return response.json()  # Assuming this returns the stream_info
        else:
            error_msg = extract_error_message(response)
            raise Exception(f"Failed to query match info.\nError Message: {error_msg}")

    def __get_video_match_count__(self, retrieve_cond: MatchInfoRetrieve) -> int:
        resp = self.query_video_match(retrieve_cond=retrieve_cond.deep_copy().set_pagination(page=1, pageSize=5))
        return resp.get('data', {}).get('total', 0)

    def retrieve_all_video_match(self, retrieve_cond: MatchInfoRetrieve):
        match_total_count = self.__get_video_match_count__(retrieve_cond=retrieve_cond)
        total_page_number = math.ceil(match_total_count / self.default_retrieve_page_size)
        print("retrieve_all_video_match, total_page_number:", total_page_number)

        # key: page, value: list<otherInfo>
        match_info_dict = {}
        cur_match_count = 0
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            futures = [executor.submit(self.query_video_match, retrieve_cond.deep_copy().set_pagination(page=i + 1,
                                                                                                        pageSize=self.default_retrieve_page_size))
                       for i in range(total_page_number)]

            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                page = result.get("data").get("page")
                match_info_list = result.get("data").get("matchInfos")
                match_info_dict[page] = match_info_list
                cur_match_count += len(match_info_list)
        match_info_list = []
        for i in range(total_page_number):
            match_info_list.extend(match_info_dict[i + 1])
        return match_info_list
