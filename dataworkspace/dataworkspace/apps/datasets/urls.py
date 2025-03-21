from django.urls import include, path

from dataworkspace.apps.accounts.utils import login_required
from dataworkspace.apps.datasets import models, views
from dataworkspace.apps.datasets.search import suggested_searches
from dataworkspace.apps.datasets.subscriptions import views as subscription_views
from dataworkspace.apps.datasets.data_dictionary import views as data_dictionary_views
from dataworkspace.apps.request_access.views import DatasetAccessRequest


urlpatterns = [
    path("", login_required(views.find_datasets), name="find_datasets"),
    path(
        "<uuid:dataset_uuid>",
        login_required(views.DatasetDetailView.as_view()),
        name="dataset_detail",
    ),
    path(
        "<uuid:dataset_uuid>/link/<uuid:source_link_id>/download",
        login_required(views.SourceLinkDownloadView.as_view()),
        name="dataset_source_link_download",
    ),
    path(
        "<uuid:dataset_uuid>/view/<uuid:source_id>/download",
        login_required(views.SourceViewDownloadView.as_view()),
        name="dataset_source_view_download",
    ),
    path(
        "<uuid:dataset_uuid>/query/<int:query_id>/download",
        login_required(views.CustomDatasetQueryDownloadView.as_view()),
        name="dataset_query_download",
    ),
    path(
        "<uuid:dataset_uuid>/query/<int:query_id>/preview",
        login_required(views.CustomDatasetQueryPreviewView.as_view()),
        name="dataset_query_preview",
    ),
    path(
        "<uuid:dataset_uuid>/table/<uuid:table_uuid>/preview",
        login_required(views.SourceTablePreviewView.as_view()),
        name="dataset_table_preview",
    ),
    path(
        "<uuid:dataset_uuid>/table/<uuid:table_uuid>/columns",
        login_required(views.SourceTableColumnDetails.as_view()),
        name="source_table_column_details",
    ),
    path(
        "<uuid:dataset_uuid>/columns",
        login_required(views.ReferenceDatasetColumnDetails.as_view()),
        name="reference_dataset_column_details",
    ),
    path(
        "<uuid:dataset_uuid>/grid",
        login_required(views.ReferenceDatasetGridView.as_view()),
        name="reference_dataset_grid",
    ),
    path(
        "<uuid:dataset_uuid>/reference/download",
        login_required(views.log_reference_dataset_download),
        name="reference_dataset_download",
    ),
    path(
        "<uuid:dataset_uuid>/eligibility-criteria",
        login_required(views.eligibility_criteria_view),
        name="eligibility_criteria",
    ),
    path(
        "<uuid:dataset_uuid>/eligibility-criteria-not-met",
        login_required(DatasetAccessRequest.as_view()),
        name="eligibility_criteria_not_met",
    ),
    path(
        "<uuid:dataset_uuid>/related-data",
        login_required(views.RelatedDataView.as_view()),
        name="related_data",
    ),
    path(
        "<uuid:dataset_uuid>/related-visualisations",
        login_required(views.RelatedVisualisationsView.as_view()),
        name="related_visualisations",
    ),
    path(
        "<uuid:dataset_uuid>/preview/<int:object_id>",
        login_required(views.DataCutPreviewView.as_view()),
        {"model_class": models.CustomDatasetQuery},
        name="data_cut_query_preview",
    ),
    path(
        "<uuid:dataset_uuid>/preview/<uuid:object_id>",
        login_required(views.DataCutPreviewView.as_view()),
        {"model_class": models.SourceLink},
        name="data_cut_source_link_preview",
    ),
    path(
        "<uuid:dataset_uuid>/toggle-bookmark",
        login_required(views.toggle_bookmark),
        name="toggle_bookmark",
    ),
    path(
        "<uuid:dataset_uuid>/set-bookmark",
        login_required(views.set_bookmark),
        name="set_bookmark",
    ),
    path(
        "<uuid:dataset_uuid>/unset-bookmark",
        login_required(views.unset_bookmark),
        name="unset_bookmark",
    ),
    path(
        "<uuid:dataset_uuid>/data-cut-usage-history",
        login_required(views.DatasetUsageHistoryView.as_view()),
        {"model_class": models.DataSet},
        name="usage_history",
    ),
    path(
        "<uuid:dataset_uuid>/visualisation-usage-history",
        login_required(views.DatasetUsageHistoryView.as_view()),
        {"model_class": models.VisualisationCatalogueItem},
        name="visualisation_usage_history",
    ),
    path(
        "<uuid:dataset_uuid>/table/<uuid:object_id>/grid",
        login_required(views.DataCutSourceDetailView.as_view()),
        {"model_class": models.SourceTable},
        name="source_table_detail",
    ),
    path(
        "<uuid:dataset_uuid>/table/<int:object_id>/grid",
        login_required(views.DataCutSourceDetailView.as_view()),
        {"model_class": models.CustomDatasetQuery},
        name="custom_dataset_query_detail",
    ),
    path(
        "<uuid:dataset_uuid>/table/<uuid:object_id>/data",
        login_required(views.DataGridDataView.as_view()),
        {"model_class": models.SourceTable},
        name="source_table_data",
    ),
    path(
        "<uuid:dataset_uuid>/table/<int:object_id>/data",
        login_required(views.DataGridDataView.as_view()),
        {"model_class": models.CustomDatasetQuery},
        name="custom_dataset_query_data",
    ),
    path(
        "reference/<int:object_id>/grid/data",
        login_required(views.ReferenceDatasetGridDataView.as_view()),
        name="reference_dataset_grid_data",
    ),
    path(
        "<uuid:dataset_uuid>/visualisation/<int:object_id>/",
        login_required(views.DatasetVisualisationView.as_view()),
        {"model_class": models.DataSet},
        name="dataset_visualisation",
    ),
    path(
        "<uuid:dataset_uuid>/visualisation-preview/<int:object_id>/",
        login_required(views.DatasetVisualisationPreview.as_view()),
        {"model_class": models.DataSet},
        name="dataset_visualisation-preview",
    ),
    path(
        "<uuid:dataset_uuid>/datacut/<int:query_id>/columns",
        login_required(views.CustomQueryColumnDetails.as_view()),
        name="custom_query_column_details",
    ),
    path(
        "<uuid:dataset_uuid>/subscription_start",
        login_required(subscription_views.DataSetSubscriptionStartView.as_view()),
        name="subscription_start",
    ),
    path(
        "<uuid:pk>/subscription_options",
        login_required(subscription_views.DataSetSubscriptionView.as_view()),
        name="subscription_options",
    ),
    path(
        "<uuid:pk>/subscription_review",
        login_required(subscription_views.DataSetSubscriptionReview.as_view()),
        name="subscription_review",
    ),
    path(
        "<uuid:subscription_id>/subscription_confirm",
        login_required(subscription_views.DataSetSubscriptionConfirm.as_view()),
        name="subscription_confirm",
    ),
    path(
        "email_preferences",
        login_required(subscription_views.current_user_email_preferences_list),
        name="email_preferences",
    ),
    path(
        "<str:subscription_id>/unsubscribe",
        login_required(subscription_views.DataSetSubscriptionUnsubscribe.as_view()),
        name="subscription_unsubscribe",
    ),
    path(
        "<uuid:dataset_uuid>/<uuid:source_id>/changelog/",
        login_required(views.SourceChangelogView.as_view()),
        {"model_class": models.SourceTable},
        name="source_table_changelog",
    ),
    path(
        "<uuid:dataset_uuid>/<str:source_id>/changelog/",
        login_required(views.SourceChangelogView.as_view()),
        {"model_class": models.CustomDatasetQuery},
        name="custom_dataset_query_changelog",
    ),
    path(
        "reference/<uuid:dataset_uuid>/changelog/",
        login_required(views.SourceChangelogView.as_view()),
        {"model_class": models.ReferenceDataset},
        name="reference_dataset_changelog",
    ),
    path(
        "<uuid:dataset_uuid>/chart/<int:object_id>/",
        login_required(views.DatasetChartView.as_view()),
        {"model_class": models.DataSet},
        name="dataset_chart",
    ),
    path(
        "<uuid:dataset_uuid>/chart/<int:object_id>/data",
        login_required(views.DatasetChartDataView.as_view()),
        {"model_class": models.DataSet},
        name="dataset_chart_data",
    ),
    path(
        "<uuid:pk>/edit-dataset",
        login_required(views.DatasetEditView.as_view()),
        name="edit_dataset",
    ),
    path(
        "<uuid:pk>/edit-visualisation-catalogue-item",
        login_required(views.VisualisationCatalogueItemEditView.as_view()),
        name="edit_visualisation_catalogue_item",
    ),
    path(
        "<uuid:pk>/search-enquiries-contact",
        login_required(views.DatasetEnquiriesContactSearchView.as_view()),
        name="search_enquiries_contact",
    ),
    path(
        "<uuid:pk>/search-secondary-enquiries-contact",
        login_required(views.DatasetSecondaryEnquiriesContactSearchView.as_view()),
        name="search_secondary_enquiries_contact",
    ),
    path(
        "<uuid:pk>/edit-permissions",
        login_required(views.DatasetEditPermissionsView.as_view()),
        name="edit_permissions",
    ),
    path(
        "<uuid:pk>/edit-permissions-summary/<int:summary_id>",
        login_required(views.DatasetEditPermissionsSummaryView.as_view()),
        name="edit_permissions_summary",
    ),
    path(
        "<uuid:pk>/search-authorized-users/<int:summary_id>",
        login_required(views.DatasetAuthorisedUsersSearchView.as_view()),
        name="search_authorized_users",
    ),
    path(
        "<uuid:pk>/add-authorized-user/<int:summary_id>/<int:user_id>",
        login_required(views.DatasetAddAuthorisedUserView.as_view()),
        name="add_authorized_user",
    ),
    path(
        "<uuid:pk>/add-authorized-users/<int:summary_id>",
        login_required(views.DatasetAddAuthorisedUsersView.as_view()),
        name="add_authorized_users",
    ),
    path(
        "<uuid:pk>/remove-authorized-user/<int:summary_id>/<int:user_id>",
        login_required(views.DatasetRemoveAuthorisedUserView.as_view()),
        name="remove_authorized_user",
    ),
    path(
        "<uuid:pk>/select-chart-source",
        login_required(views.SelectChartSourceView.as_view()),
        name="select_chart_source",
    ),
    path(
        "<uuid:pk>/filter-chart-data/<str:source_id>/",
        login_required(views.FilterChartDataView.as_view()),
        name="filter_chart_data",
    ),
    path(
        "<uuid:dataset_uuid>/aggregate-chart-data/<str:source_id>/",
        login_required(views.AggregateChartDataViewView.as_view()),
        name="aggregate_chart_data",
    ),
    path(
        "<uuid:dataset_uuid>/grid-chart/<str:source_id>/",
        login_required(views.CreateGridChartView.as_view()),
        name="create_chart_from_grid",
    ),
    path(
        "<uuid:dataset_uuid>/charts/",
        login_required(views.DatasetChartsView.as_view()),
        name="dataset_charts",
    ),
    path(
        "<uuid:pk>/manage/",
        include(
            ("dataworkspace.apps.datasets.manager.urls", "dataset_manager"),
            namespace="manager",
        ),
    ),
    path(
        "data-dictionary/<uuid:source_uuid>",
        login_required(data_dictionary_views.DataDictionaryView.as_view()),
        name="data_dictionary",
    ),
    path(
        "<uuid:dataset_uuid>/edit-data-dictionary/<uuid:source_uuid>",
        login_required(data_dictionary_views.DataDictionaryEditView.as_view()),
        name="edit_data_dictionary",
    ),
    path(
        "<str:schema_name>/find-data-dictionary/<str:table_name>",
        login_required(data_dictionary_views.find_data_dictionary_view),
        name="find_data_dictionary",
    ),
    path(
        "find_suggested_searches",
        login_required(suggested_searches),
        name="find_suggested_searches",
    ),
    path(
        "log_data_preview_load_time/<uuid:dataset_uuid>/<str:source_id>/",
        login_required(views.log_data_preview_load_time),
        name="log_data_preview_load_time",
    ),
]
